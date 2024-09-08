# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/7 19:24
# File:app

import os
import sys
from datetime import datetime
from typing import Optional
from PySide6.QtCore import Qt, QLocale, QTranslator, QDateTime
from PySide6.QtGui import QIcon, QFontMetrics
from PySide6.QtWidgets import QApplication, QFileDialog, QTableWidgetItem, QMainWindow, QDialog, \
    QHeaderView, QStyleOptionViewItem, QStyle, QStyledItemDelegate, QScrollArea, QFrame, QLabel, QVBoxLayout
from loguru import logger
from qfluentwidgets.common import FluentIcon as FIF
from win32file import CreateFile, SetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
import res_rc
import win32timezone
from qfluentwidgets import *
from ui import Ui_MainWindow
from ui_sec_menu import Ui_Dialog
from qfluentwidgets import setThemeColor, setTheme, Theme
from enum import Enum
from prettytable import PrettyTable

logger.add(
    os.path.join(os.getcwd(), "log.log"),
    rotation="10 MB",
    retention="10 days",
    level="DEBUG",
)


class UserFormChangeMode(Enum):
    new = 0
    path = 1
    local_time = 2
    global_time = 3


# class CustomMessageBox(MessageBoxBase):
#     """ Custom message box """
#
#     def __init__(self, title: str, content: str, parent=None):
#         super().__init__(parent=parent)
#         scroller = SmoothScrollArea(parent)
#         widget = QFrame(parent, objectName='centerWidget')
#         self.scrollLayout = ScrollArea(widget)
#         self.scrollLayout.setWidget(scroller)
class MyDialog(Dialog):
    """ Custom message box """

    def __init__(self, title: str, content: str, parent=None):
        super().__init__(title, content, parent=parent)
        # scroller = SmoothScrollArea(parent)
        # self.scrollLayout = ScrollArea(self.contentLabel)
        # self.scrollLayout.setWidget(scroller)


class SecDialog(QDialog, Ui_Dialog):  # 二级菜单窗口
    signal_time_data = Signal(str)

    def __init__(self, logo):
        super(SecDialog, self).__init__()
        self.sd = Ui_Dialog()
        self.sd.setupUi(self)
        self.setWindowTitle('设置时间')
        self.setWindowIcon(logo)
        self.init_sec_table()
        self.init_sec_time()
        self.sec_band()

    def init_sec_time(self):
        self.sd.calendar_picker_ymd.setDate(QDateTime.currentDateTime().date())
        self.sd.time_picker_hms.setTime(QDateTime.currentDateTime().time())

    def init_sec_table(self):
        self.sd.table_widget_sec_info_bar.setColumnCount(1)
        self.sd.table_widget_sec_info_bar.setRowCount(2)
        self.sd.table_widget_sec_info_bar.setVerticalHeaderLabels(['当前选择路径'])
        self.sd.table_widget_sec_info_bar.setHorizontalHeaderLabels(['更多详细信息'])
        self.sd.table_widget_sec_info_bar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.sd.table_widget_sec_info_bar.setItemDelegate(
            CustomDelegate(self.sd.table_widget_sec_info_bar))

    def sec_band(self):
        self.sd.push_button_ok.clicked.connect(self.close)
        self.sd.table_widget_sec_info_bar.itemEntered.connect(self.update_sec_tooltip)

    def update_sec_tooltip(self, item):
        if item is None:
            return
        row: int = item.row()
        col: int = item.column()
        title: str = self.sd.table_widget_sec_info_bar.verticalHeaderItem(col).text()
        file_path: str = self.sd.table_widget_sec_info_bar.item(row, col).text()
        self.sd.table_widget_sec_info_bar.setToolTip(f'{title}:{file_path}')

    def ymd_hms(self) -> str:
        ymd = self.sd.calendar_picker_ymd.getDate()
        hms = self.sd.time_picker_hms.getTime()
        year = ymd.year()
        month = ymd.month()
        day = ymd.day()
        hour = hms.hour()
        minute = hms.minute()
        second = hms.second()
        # 构造日期时间字符串
        formatted_string = f"{year}年{month}月{day}日 {hour:02}:{minute:02}:{second:02}"
        return formatted_string

    def close(self):
        emit_time: str = self.ymd_hms()
        if self.signal_time_data.emit(emit_time):  # 确保正常发送了时间信息再关闭窗口
            super().close()


class CustomDelegate(TableItemDelegate):
    left_double_click_signal_pos_data = Signal(tuple)

    def createEditor(self, parent, option, index):
        pos: tuple = (index.row(), index.column())
        self.left_double_click_signal_pos_data.emit(pos)  # 发送双击位置


class APP(QMainWindow, Ui_MainWindow):
    software_name = 'FileDateChanger'
    software_name_version = '0.4'
    software_name_author = 'Gentlesprite'
    software_name_simplified_chinese = '文件日期修改器'
    software_name_author_simplified_chinese = '雪碧'
    software_title = ' '.join([software_name_simplified_chinese, f'[{software_name}]', '作者:',
                               software_name_author_simplified_chinese + f'({software_name_author})'])
    software_logo = ':/logo0.4.ico'
    software_theme_color = '#28afe9'

    software_theme_mode = Theme.DARK
    default_path = os.path.abspath(os.getcwd())

    def __init__(self):
        super(APP, self).__init__()
        self.file_name: list = []  # 存储路径->[路径]
        self.file_info: dict = {}  # 存储->{路径:[创建时间,修改时间,访问时间]}
        self.current_left_click_row: int = 0  # 初始化当前鼠标左键单击的行
        self.current_left_click_column: int = 0  # 初始化当前鼠标左键单击的列
        self.current_right_click_row: int = 0  # 初始化当前鼠标右键单击的行
        self.current_right_click_column: int = 0  # 初始化当前鼠标右键单击的列
        self.current_left_double_click_row: int = 0  # 初始化当前鼠标左键双击的列
        self.current_left_double_click_column: int = 0  # 初始化当前鼠标左键双击的列
        self.open_dir_path: str = APP.default_path  # 初始化选择文件夹打开的路径
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        APP.init_theme()  # 初始化主题
        self.ui.tool_button_open_dir.setIcon(FIF.MORE.icon())  # 设置打开文件夹的按钮图标
        self.delegate: CustomDelegate = ...  # 定义表格自定义委托
        self.dialog = SecDialog(QIcon(APP.software_logo))  # 用户变更时间的二级窗口
        self.setWindowTitle(APP.software_title)
        self.setWindowIcon(QIcon(APP.software_logo))
        self.init_global_time_setting()  # 初始化全局时间
        self.init_table()  # 初始化表格内容
        self.band()  # 初始化绑定按键

    @staticmethod
    def init_theme():
        setThemeColor(APP.software_theme_color)  # 设置主题颜色
        setTheme(APP.software_theme_mode)  # 设置暗色主题

    def init_global_time_setting(self):
        self.ui.calendar_picker_ymd.setDate(QDateTime.currentDateTime().date())
        self.ui.time_picker_hms.setTime(QDateTime.currentDateTime().time())

    def init_table(self):
        self.ui.table_widget_info_bar.setContextMenuPolicy(Qt.CustomContextMenu)  # 打开右键菜单策略
        self.ui.table_widget_info_bar.setBorderRadius(8)
        self.ui.table_widget_info_bar.setWordWrap(False)
        self.ui.table_widget_info_bar.setRowCount(-1)
        self.ui.table_widget_info_bar.setColumnCount(4)
        self.ui.table_widget_info_bar.setColumnWidth(0, 230)
        self.ui.table_widget_info_bar.setHorizontalHeaderLabels(['路径', '创建时间', '修改时间', '访问时间'])
        self.ui.table_widget_info_bar.setBorderVisible(True)
        self.delegate: CustomDelegate = CustomDelegate(self.ui.table_widget_info_bar)  # 将表格功能进行自定义委托
        self.ui.table_widget_info_bar.setItemDelegate(self.delegate)
        self.ui.table_widget_info_bar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 该条设置列自适应宽度
        # 该条设置列最小宽度，防止拉伸改变表头宽度的时候，宽度小于最小宽度，以至于表头文字内容消失，显示异常
        self.ui.table_widget_info_bar.horizontalHeader().setMinimumSectionSize(100)

        # # 该条设置第一列可以自由拉伸，此时拉伸的前提有1和2，即没有特殊要求的情况下，全部列自适应宽度
        # self.ui.table_widget_info_bar.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)

        # self.ui.table_widget_info_bar.setContextMenuPolicy(Qt.CustomContextMenu)  # 设置策略为自定义菜单
        self.ui.table_widget_info_bar.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.ui.table_widget_info_bar.horizontalHeader().setMaximumSectionSize(400)  # 设置最大宽度为200像素

    def band(self):
        self.ui.push_button_change_time.clicked.connect(self.change_file_time)
        self.ui.tool_button_open_dir.clicked.connect(lambda: self.open_dir_mode(change_mode=UserFormChangeMode.new))
        self.ui.text_edit_path_input.signal_drop.connect(self.drop_mode)
        self.ui.text_edit_path_input.signal_paste.connect(self.paste_mode)
        self.ui.text_edit_path_input.textChanged.connect(
            lambda: self.typing_mode(self.ui.text_edit_path_input.toPlainText()))
        self.ui.table_widget_info_bar.itemClicked.connect(self.set_table)
        self.ui.table_widget_info_bar.cellClicked.connect(self.receive_left_clicked_pos)
        self.ui.table_widget_info_bar.customContextMenuRequested.connect(self.receive_right_clicked_pos)
        self.ui.table_widget_info_bar.itemEntered.connect(self.update_tooltip)

        self.ui.calendar_picker_ymd.dateChanged.connect(self.
                                                        receive_global_ymd)
        self.ui.time_picker_hms.timeChanged.connect(self.receive_global_hms)
        self.delegate.left_double_click_signal_pos_data.connect(self.receive_left_double_clicked_pos)
        # self.dialog.signal_time_data.connect(self.receive_time_data)
        self.dialog.signal_time_data.connect(lambda res: self.set_table(
            change_mode=UserFormChangeMode.local_time,
            data=(res, self.current_left_double_click_row, self.current_left_double_click_column)
        ))

    def receive_global_ymd(self, time):
        """
        :param time:
            全局时分秒变量,
            更改到表格中
            同时更新self.file_name和self.file_info
        :return:
        """
        ymd_str = datetime(time.year(), time.month(), time.day()).strftime('%Y年%#m月%#d日')
        if self.file_info:
            file_info = self.file_info.copy()

            for path, timestamps in file_info.items():
                if not isinstance(timestamps, list) or len(timestamps) != 3:
                    raise ValueError(f"Incorrect timestamp format for file path '{path}'")

                create_time, modify_time, access_time = timestamps

                # 提取并保留原有的时分秒
                create_hms = create_time.split(' ')[-1]
                modify_hms = modify_time.split(' ')[-1]
                access_hms = access_time.split(' ')[-1]

                # 将新的年月日与旧的时分秒拼接
                if self.ui.check_box_create_time.isChecked():
                    create_time = f"{ymd_str} {create_hms}"
                if self.ui.check_box_modify_time.isChecked():
                    modify_time = f"{ymd_str} {modify_hms}"
                if self.ui.check_box_access_time.isChecked():
                    access_time = f"{ymd_str} {access_hms}"

                file_info[path] = [create_time, modify_time, access_time]

            self.file_info = file_info
            self.set_table(change_mode=UserFormChangeMode.global_time)
            logger.debug("File info: {}".format(file_info))
        else:
            print("Warning: `self.file_info` is empty. No updates were made.")

    def receive_global_hms(self, time) -> None:
        """
        :param time:
            全局时分秒变量,
            更改到表格中
            同时更新self.file_name和self.file_info
        :return:
        """
        hms_str = f"{time.hour():02d}:{time.minute():02d}:{time.second():02d}"  # 使用f-string直接格式化时分秒
        if self.file_info:
            file_info = self.file_info.copy()

            for path, timestamps in file_info.items():
                if not isinstance(timestamps, list) or len(timestamps) != 3:
                    raise ValueError(f"Incorrect timestamp format for file path '{path}'")

                create_time, modify_time, access_time = timestamps

                # 提取并保留原有的年月日
                create_ymd = ' '.join(create_time.split(' ')[:-1])
                modify_ymd = ' '.join(modify_time.split(' ')[:-1])
                access_ymd = ' '.join(access_time.split(' ')[:-1])

                # 将新的时分秒与旧的年月日拼接
                if self.ui.check_box_create_time.isChecked():
                    create_time = f"{create_ymd} {hms_str}"
                if self.ui.check_box_modify_time.isChecked():
                    modify_time = f"{modify_ymd} {hms_str}"
                if self.ui.check_box_access_time.isChecked():
                    access_time = f"{access_ymd} {hms_str}"

                file_info[path] = [create_time, modify_time, access_time]

            self.file_info = file_info
            self.set_table(change_mode=UserFormChangeMode.global_time)
            logger.debug("File info: {}".format(file_info))
        else:
            print("Warning: `self.file_info` is empty. No updates were made.")

    def update_tooltip(self, item) -> None:
        """
        更新鼠标悬浮提示
        :param item:行和列
        :return:
        """
        if item is None:
            return
        row: int = item.row()
        col: int = item.column()
        title: str = self.ui.table_widget_info_bar.horizontalHeaderItem(col).text()
        file_path: str = self.ui.table_widget_info_bar.item(row, col).text()
        self.ui.table_widget_info_bar.setToolTip(f'{title}:{file_path}')

    def receive_left_double_clicked_pos(self, pos: tuple) -> None:
        """
        接收鼠标左键双击的行、列数据,
        并实时更新到->self.left_double_click_row, self.left_double_click_column,
        实现全局引用。
        并能根据行列不同,触发不同的事件。
            鼠标左键双击路径列(0)->触发修改文件事件(open_dir_mode)
            鼠标左键双击路径列(1-3)->触发修改日期事件(open_time_picker_dialog)
        :param pos:
            类型:tuple
            记录行和列的元祖
        :return:
            None
        """
        self.current_left_double_click_row: int = pos[0]
        self.current_left_double_click_column: int = pos[1]
        if self.current_left_double_click_column == 0:
            self.open_dir_mode(change_mode=UserFormChangeMode.path, pos=pos)
        elif self.current_left_double_click_column in range(1, 4):
            self.open_time_picker_dialog(pos)

    def receive_left_clicked_pos(self, row: int, column: int) -> None:  # 实时更新点击的行和列
        """
        接收鼠标左键单击的行、列数据,
        并实时更新到->self.current_left_click_row,self.current_left_click_column,
        实现全局引用。
        并能根据行列的不同,触发不同的事件。
        :param row:
            类型:int
            记录行
        :param column:
            类型:int
            记录列
        :return:
            None
        """
        # logger.debug(f'点击了第行:{row},列:{column}')
        self.current_left_click_row: int = row
        self.current_left_click_column: int = column
        if column == 0:
            ...
            # 定义左键单击路径列事件
        elif column in range(1, 4):
            logger.debug(f'点击了第行:{row},列:{column}')
            time: str = self.ui.table_widget_info_bar.item(row, column).text()  # 拿到对应表格时间
            q_time: QDateTime = QDateTime.fromString(time, "yyyy年M月d日 H:mm:ss")
            self.ui.calendar_picker_ymd.dateChanged.disconnect()
            self.ui.time_picker_hms.timeChanged.disconnect()
            self.ui.calendar_picker_ymd.setDate(q_time.date())
            self.ui.time_picker_hms.setTime(q_time.time())
            self.ui.calendar_picker_ymd.dateChanged.connect(self.
                                                            receive_global_ymd)
            self.ui.time_picker_hms.timeChanged.connect(self.receive_global_hms)
            # 定义左键单击时间列事件

    def receive_right_clicked_pos(self, pos: tuple) -> None:
        """
        接收鼠标右键单击的行、列数据,
        并实时更新到->self.current_right_click_row,self.current_right_click_column,
        实现全局引用。
        :param pos:
            类型:tuple
            记录行和列的元祖
        :return:
            None
        """
        menu = RoundMenu()
        if self.file_info and self.file_name:
            self.current_right_click_row: int = self.ui.table_widget_info_bar.rowAt(pos.y())  # 获取当前右键的行
            self.current_right_click_column: int = self.ui.table_widget_info_bar.columnAt(pos.x())  # 获取当前右键的列
            path_pos = self.current_right_click_row, 0
            create_time_pos = self.current_right_click_row, 1
            modify_time_pos = self.current_right_click_row, 2
            access_time_pos = self.current_right_click_row, 3
            # menu.addAction(Action(icon=FIF.ROTATE.icon(), text=self.tr('单独修改(当前项)'), parent=self,
            #                       triggered=lambda: self.single_change()))
            # menu.addSeparator()
            menu.addAction(Action(icon=FIF.ADD.icon(), text=self.tr('添加新文件'), parent=self,
                                  triggered=lambda: self.open_dir_mode(change_mode=UserFormChangeMode.new)), )
            menu.addSeparator()
            menu.addActions([Action(icon=FIF.FOLDER.icon(), text=self.tr('修改文件路径'), parent=self,
                                    triggered=lambda: self.open_dir_mode(change_mode=UserFormChangeMode.path,
                                                                         pos=path_pos)),
                             Action(icon=FIF.HISTORY.icon(), text=self.tr('变更创建时间'), parent=self,
                                    triggered=lambda: self.open_time_picker_dialog(create_time_pos)),
                             Action(icon=FIF.LABEL.icon(), text=self.tr('变更修改时间'), parent=self,
                                    triggered=lambda: self.open_time_picker_dialog(modify_time_pos)),
                             Action(icon=FIF.ZOOM_OUT.icon(), text=self.tr('变更访问时间'), parent=self,
                                    triggered=lambda: self.open_time_picker_dialog(access_time_pos))])
        else:
            menu.addAction(Action(FIF.ADD.icon(), self.tr('添加新文件'), self,
                                  triggered=lambda: self.open_dir_mode(change_mode=UserFormChangeMode.new))
                           )
        menu.exec(self.ui.table_widget_info_bar.mapToGlobal(pos))

    @staticmethod
    def get_file_time(file_path: str) -> list:
        """
        得到文件的创建日期,修改日期,访问日期
        :param file_path:
            类型:str
            需要得到日期列表的路径
        :return:
            类型:list
            [创建日期,修改日期,访问日期]
        """
        time_format: str = '%Y年%#m月%#d日 %H:%M:%S'
        create_time: str = datetime.fromtimestamp(os.path.getctime(file_path)).strftime(time_format)
        modify_time: str = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime(time_format)
        access_time: str = datetime.fromtimestamp(os.path.getatime(file_path)).strftime(time_format)
        return [create_time, modify_time, access_time]

    def _process_new_table(self):
        for file_path in self.file_name:
            # 检查当前项是否已经存在于表格中
            exists: bool = False
            for row in range(self.ui.table_widget_info_bar.rowCount()):
                item: QTableWidgetItem = self.ui.table_widget_info_bar.item(row, 0)
                if item is not None and item.text() == file_path:
                    exists: bool = True
                    break
            # 如果当前项不存在于表格中，则添加
            if not exists:
                row_position = self.ui.table_widget_info_bar.rowCount()
                self.ui.table_widget_info_bar.insertRow(row_position)
                # 添加路径
                path_item = QTableWidgetItem(file_path)
                self.ui.table_widget_info_bar.setItem(row_position, 0, path_item)
                # 获取文件的创建时间、修改时间和访问时间
                file_stat = os.stat(file_path)
                create_time, modify_time, access_time = APP.get_file_time(file_path)
                create_time_item: QTableWidgetItem = QTableWidgetItem(create_time)
                modify_time_item: QTableWidgetItem = QTableWidgetItem(modify_time)
                access_time_item: QTableWidgetItem = QTableWidgetItem(access_time)
                self.ui.table_widget_info_bar.setItem(row_position, 1, create_time_item)
                self.ui.table_widget_info_bar.setItem(row_position, 2, modify_time_item)
                self.ui.table_widget_info_bar.setItem(row_position, 3, access_time_item)
                self.file_info[file_path] = [create_time, modify_time, access_time]
                self.ui.table_widget_info_bar.scrollToItem(path_item)

    def set_table(self, change_mode: UserFormChangeMode = UserFormChangeMode.new,
                  **kwargs: Optional[tuple]) -> None:  # 增
        if change_mode == UserFormChangeMode.new:
            self._no_signal_change_text()
            self._process_new_table()
        elif change_mode == UserFormChangeMode.path:
            new_path, row, column = kwargs['data']
            if new_path:
                new_path = os.path.normpath(new_path)  # 格式化路径
                # 获取替换文件的时间
                create_time, modify_time, access_time = self.get_file_time(new_path)
                # 通过当前点击行列数来获取当前第一列的路径数据
                logger.debug(f'原来的字典为{self.file_info},列表为{self.file_name}')
                path: str = self.ui.table_widget_info_bar.item(row, 0).text()  # 获取原来列表的键
                for old_key in list(self.file_info.keys()):
                    logger.error(f'原来的路径{old_key},现在替换的路径{new_path}')
                    if old_key == path:
                        self.file_info.pop(old_key)
                        self.file_name.remove(old_key)
                        self.file_info[new_path] = [create_time, modify_time, access_time]
                        self.file_name.append(new_path)
                        break
                self._no_signal_change_text()
                # 将字符串转换为Qtable对象
                create_time_item: QTableWidgetItem = QTableWidgetItem(create_time)
                modify_time_item: QTableWidgetItem = QTableWidgetItem(modify_time)
                access_time_item: QTableWidgetItem = QTableWidgetItem(access_time)
                new_path_item: QTableWidgetItem = QTableWidgetItem(new_path)
                self.ui.table_widget_info_bar.setItem(row, 0, new_path_item)
                self.ui.table_widget_info_bar.setItem(row, 1, create_time_item)
                self.ui.table_widget_info_bar.setItem(row, 2, modify_time_item)
                self.ui.table_widget_info_bar.setItem(row, 3, access_time_item)
                logger.debug(f'已修改: {path} -> {new_path}')
                logger.debug(f'当前字典为{self.file_info},列表为{self.file_name}')
        elif change_mode == UserFormChangeMode.local_time:
            new_time, row, column = kwargs['data']
            path: str = self.ui.table_widget_info_bar.item(row, 0).text()
            match_value: list = self.file_info[path]
            logger.debug(f'找到路径:{path}对应的日期为:{match_value}')
            match_value[self.current_left_click_column - 1] = new_time  # 列数-1得到对应索引值[创建时间,修改时间,访问时间]
            logger.debug(f'当前更新的字典为:{self.file_info}')
            item_ymd = QTableWidgetItem(new_time)  # 转化为QTableWidgetItem对象
            self.ui.table_widget_info_bar.setItem(row, column, item_ymd)  # 更新到面板中
        elif change_mode == UserFormChangeMode.global_time:
            # 获取最新的文件信息字典
            info_bar: dict = self._get_all_items()
            # 更新info_bar中与self.file_info有差异的条目
            for path, timestamps in self.file_info.items():
                if path in info_bar:
                    old_timestamps = info_bar[path]
                    if old_timestamps != timestamps:
                        info_bar[path] = timestamps
                        row_index = self._find_table_row_by_path(path)
                        if row_index is not None:
                            for col_index, timestamp in enumerate(timestamps, start=1):
                                item = QTableWidgetItem(timestamp)
                                self.ui.table_widget_info_bar.setItem(row_index, col_index, item)
                        else:
                            logger.warning(f"Row for path '{path}' not found in the table.")
                else:
                    logger.warning(f"Path '{path}' from self.file_info not found in the table.")

            logger.info(
                "Updated QTableWidget with the latest file information from self.file_info where values differ.")

    def _find_table_row_by_path(self, path: str) -> Optional[int]:
        total_rows = self.ui.table_widget_info_bar.rowCount()

        for row_index in range(total_rows):
            path_item = self.ui.table_widget_info_bar.item(row_index, 0)
            if path_item is not None and path_item.text() == path:
                return row_index

        return None

    def delete_content(self, content_to_delete: str) -> None:  # 删除对应内容的项
        # 查找需要删除的项的行索引
        row_index: int = -1
        for row in range(self.ui.table_widget_info_bar.rowCount()):
            item = self.ui.table_widget_info_bar.item(row, 0)  # 假设内容在第一列
            if item.text() == content_to_delete:
                row_index = row
                break
        if row_index != -1:
            # 删除行
            self.ui.table_widget_info_bar.removeRow(row_index)
            logger.debug(f'已删除: {content_to_delete}')
            # 从文件名列表中也移除
            self.file_name.remove(content_to_delete)
            self.file_info.pop(content_to_delete)
            self.ui.table_widget_info_bar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        else:
            logger.debug(f'要删除的内容 "{content_to_delete}" 未找到')

    def _get_all_items(self):
        # 获取行数和列数
        total_rows: int = self.ui.table_widget_info_bar.rowCount()  # 行
        # 初始化字典，用于存储文件路径及其对应的时间戳
        all_items: dict = {}
        # 遍历所有行
        for row in range(total_rows):
            # 初始化当前行的字典项
            # 依次获取文件路径、创建时间、修改时间和访问时间
            for column in range(4):
                item: QTableWidgetItem = self.ui.table_widget_info_bar.item(row, column)
                if item is not None:
                    text = item.text()
                    if column == 0:  # 文件路径
                        current_row_key = text
                    else:  # 时间戳
                        if current_row_key not in all_items:
                            all_items[current_row_key] = []
                        all_items[current_row_key].append(text)
        return all_items

    def _no_signal_change_text(self):
        self.ui.text_edit_path_input.textChanged.disconnect()
        self.ui.text_edit_path_input.setText('\n'.join(self.file_name) if self.file_name else '')
        self.ui.text_edit_path_input.textChanged.connect(
            lambda: self.typing_mode(self.ui.text_edit_path_input.toPlainText()))

    def open_dir_mode(self, change_mode=UserFormChangeMode.new, **kwargs):  # 打开文件夹模式

        self.open_dir_path = APP.default_path if not os.path.isdir(self.open_dir_path) else self.open_dir_path
        if change_mode == UserFormChangeMode.new:
            data: list = [os.path.normpath(i) for i in
                          QFileDialog.getOpenFileNames(self, "选择文件", self.open_dir_path, "All Files (*)")[
                              0]]
            self.open_dir_path = os.path.dirname(os.path.normpath(data[-1])) if data else self.open_dir_path
            if self.file_name:
                for i in data:
                    if i.lower() not in [f.lower() for f in self.file_name]:
                        self.file_name.append(i)
                    else:
                        logger.warning(f'{i}已存在!')
            else:
                self.file_name = data
            self.set_table(change_mode=change_mode)
        elif change_mode == UserFormChangeMode.path:
            # todo:当前有项才能选择
            if self.file_info:  # 首先判断表中要有项
                pos: tuple = kwargs['pos']  # 再得到鼠标选择的表格位置
                new_key: str = QFileDialog.getOpenFileName(self, "选择文件", self.open_dir_path, "All Files (*)")[0]
                # 加入对项中已存在的文件进行判断
                if os.path.normpath(new_key) in self.file_name:
                    logger.warning(f'{new_key}已存在!')
                else:
                    data: tuple = new_key, pos[0], pos[1]
                    logger.debug(data)
                    self.set_table(change_mode=UserFormChangeMode.path, data=data)
            else:
                logger.error(self.tr('未选择任何项'))

    def open_time_picker_dialog(self, pos):
        try:
            if pos and self.file_name and self.file_info:
                logger.debug(pos)
                row, column = pos
                q_format = "yyyy年M月d日 H:mm:ss"
                path = self.ui.table_widget_info_bar.item(row, 0).text()  # 得到路径
                self.dialog.sd.table_widget_sec_info_bar.setItem(0, 0, QTableWidgetItem(path))  # 设置路径到表格中
                self.dialog.sd.table_widget_sec_info_bar.setToolTip(f'路径:{path}')

                create_time, modify_time, access_time = self.get_file_time(file_path=path)  # 得到日期信息
                text: str = ''
                time_type: str = ''
                if column == 1:
                    text = '当前创建时间'
                    time_type: str = create_time

                elif column == 2:
                    text: str = '当前修改时间'
                    time_type: str = modify_time
                elif column == 3:
                    text: str = '当前访问时间'
                    time_type: str = access_time
                # 获取点击的内容的时间
                q_time: QDateTime = QDateTime.fromString(time_type, q_format)
                self.dialog.sd.calendar_picker_ymd.setDate(q_time.date())
                self.dialog.sd.time_picker_hms.setTime(q_time.time())  # 设置与点击内容一致的时间

                self.dialog.setWindowTitle(text.replace('当前', '变更'))
                self.dialog.sd.table_widget_sec_info_bar.setItem(1, 0, QTableWidgetItem(time_type))
                self.dialog.sd.table_widget_sec_info_bar.setVerticalHeaderItem(1, QTableWidgetItem(text))
                self.dialog.exec()
            else:
                logger.error('未找到任何项')
        except Exception as e:
            logger.error(e)

    def drop_mode(self, data: list) -> None:  # 拖入模式
        for i in data:
            if i.lower() not in [f.lower() for f in self.file_name]:
                self.file_name.append(i)
        self.set_table(change_mode=UserFormChangeMode.new)

    def paste_mode(self, path):
        if self.file_name:
            for i in path:
                if i.lower() not in [f.lower() for f in self.file_name]:
                    self.file_name.append(i)
        else:
            self.file_name = path
        self.set_table(change_mode=UserFormChangeMode.new)

    def typing_mode(self, res) -> None:
        # 检查用户是否完成了输入
        file_names: list = res.rstrip('\n').split('\n')
        if res and res.endswith('\n'):
            # 以 '\n' 分隔文本
            # 遍历分隔后的文件名
            for file_name in file_names:
                # 去除首尾空白字符
                file_name = file_name.strip()

                # 如果文件名存在，并且不在列表中，则添加到列表中
                if file_name and os.path.exists(file_name) and file_name.lower() not in [f.lower() for f in
                                                                                         self.file_name]:
                    self.file_name.append(os.path.normpath(file_name))
            # 存储路径
            self._process_new_table()
            logger.debug(f'手动输入内容发生改变:{self.file_name}')
        else:
            need_remove: list = [f for f in self.file_name if f not in file_names]
            for item in need_remove:
                self.delete_content(item)
            self._process_new_table()

    def show_message(self, message, title='提示'):
        #
        pm = MessageBox(title=title, content=message, parent=self)

        pm.show()

    def checker(func):
        def wrapper(self, *args, **kwargs):
            ymd = self.ui.calendar_picker_ymd.getDate()
            hms = self.ui.time_picker_hms.getTime()
            path: str = self.ui.text_edit_path_input.toPlainText().strip()  # 去除首尾空白字符

            # 用于显示错误消息的统一函数

            if not path:
                self.show_message('内容为空!')
                return
            if ymd.isNull():
                self.show_message('未选择年月日!')
                return
            if hms.isNull():
                self.show_message('未选择时分秒!')
                return
            # 判断路径是否以'&'结尾，且是否为有效路径
            if not path.endswith('\n') and os.path.exists(path):
                # 如果是有效路径，则在末尾添加'&'
                new_path = path + '\n'
                logger.warning(f'路径没有以&结尾,已自动添加:{new_path}')
                self.ui.text_edit_path_input.setText(new_path)
            elif not path.endswith('\n'):
                # 处理多路径情况
                res = path.rstrip('\n').split('\n')
                valid_paths = []
                for i in res:
                    if os.path.exists(i):
                        valid_paths.append(i + '\n')
                        logger.debug(f'有效路径:{i}\n')
                    else:
                        logger.warning(f'路径不存在:{i}')
                if valid_paths:
                    # 如果有有效路径，则将它们拼接起来
                    new_path = ''.join(valid_paths)
                    self.ui.text_edit_path_input.setText(new_path)
                else:
                    # 如果没有有效路径，则不执行原函数
                    self.show_message('没有有效的路径。')
                    return
            # 执行原函数
            return func(self, *args, **kwargs)

        return wrapper

    @checker
    def change_file_time(self):
        result: dict = {}
        logger.debug(f'所有文件路径{self.file_name},时间信息{self.file_info}')
        for file_name, time_info in self.file_info.items():
            create_time, modify_time, access_time = time_info
            create_time_stamp = datetime.strptime(create_time, '%Y年%m月%d日 %H:%M:%S').timestamp()
            modify_time_stamp = datetime.strptime(modify_time, '%Y年%m月%d日 %H:%M:%S').timestamp()
            access_time_stamp = datetime.strptime(access_time, '%Y年%m月%d日 %H:%M:%S').timestamp()
            _file_path, _result, _reason = APP._change_file_time(file_path=file_name, create_time=create_time_stamp,
                                                                 modify_time=modify_time_stamp,
                                                                 access_time=access_time_stamp)
            result[_file_path] = [_result, _reason]
        logger.debug(result)
        pt_from = PrettyTable(['文件路径', '错误原因'])
        _info = []
        error_info: dict = {}
        for i in result.items():
            _info.append(i)
        for j in _info:
            if j[1][0] is False:
                print(j[0],j[1][1])
                error_info[j[0]] = f'{j[1][1]}'
        print(error_info)
        ei = '\n'.join([f'文件{j[0]} 原因:{j[1]}' for j in error_info.items()])

        if error_info:
            MyDialog(title='修改状态', content=f'找到如下错误信息:\n{ei}\n其余全部修改成功').show()
        else:
            MyDialog(title='修改状态', content=f'修改成功').show()

    @staticmethod
    def print_univ_list(u_list, num):
        tplt = "{0:{2}^10}\t{1:{2}^10}\t"
        print(tplt.format('文件路径', '错误原因', chr(12288)))
        for n in range(num):
            u = u_list[n]
            return tplt.format(u[0], u[1], u[2], chr(12288))

    @staticmethod
    def _change_file_time(file_path: str, create_time: float, modify_time: float, access_time: float):
        """
        用来修改任意文件的相关时间属性，时间格式：时间戳
        :param file_path: 文件路径名
        :param create_time: 创建时间（时间戳）
        :param modify_time: 修改时间（时间戳）
        :param access_time: 访问时间（时间戳）
        """
        result: bool = False
        reason = None
        try:
            fh = CreateFile(file_path, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
            create_time = datetime.fromtimestamp(create_time)
            access_time = datetime.fromtimestamp(access_time)
            modify_time = datetime.fromtimestamp(modify_time)
            SetFileTime(fh, create_time, access_time, modify_time)
            CloseHandle(fh)
            result = True
        except Exception as error:
            reason = error
        return file_path, result, reason

    @staticmethod
    def setDpiFromWindowsSettings():
        """
        根据windows的DPI缩放来适配软件的DPI
        :return:
        """
        QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Ceil)


if __name__ == "__main__":
    APP.setDpiFromWindowsSettings()
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    translator = QTranslator()
    translator.load(QLocale.system(), ":/lan/qfluentwidgets_")
    app.installTranslator(translator)
    w = APP()
    w.show()
    sys.exit(app.exec())
