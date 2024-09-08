# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/7 19:24
# File:app

import os
import sys
from datetime import datetime
from typing import Optional
from PySide2.QtCore import Qt, QLocale, QTranslator, Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QVBoxLayout, QFileDialog, QTableWidgetItem, QMainWindow, QDialog, \
    QHeaderView, QAction
from loguru import logger
from qfluentwidgets import FlyoutViewBase, BodyLabel, PrimaryPushButton
from qfluentwidgets import TableItemDelegate
from qfluentwidgets.components.dialog_box import MessageBox
from win32file import CreateFile, SetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
import res_rc
from ui import Ui_MainWindow
from ui_sec_menu import Ui_Dialog
from enum import Enum
from qfluentwidgets import StyleSheetBase, Theme, qconfig, RoundMenu
from qfluentwidgets.common import FluentIcon as FIF

logger.add(
    os.path.join(os.getcwd(), "log.log"),
    rotation="10 MB",
    retention="10 days",
    level="DEBUG",
)


class UserFormChangeMode(Enum):
    new = 0
    path = 1
    time = 2


class StyleSheet(StyleSheetBase, Enum):
    """ Style sheet  """

    WINDOW = "APP"

    def path(self, theme=Theme.AUTO):
        theme = qconfig.theme if theme == Theme.AUTO else theme
        return f"qss/{theme.value.lower()}/{self.value}.qss"


class SecDialog(QDialog, Ui_Dialog):
    signal_time_data = Signal(str)

    def __init__(self):
        super(SecDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def close(self):
        emit_time: str = self.ymd_hms()
        if self.signal_time_data.emit(emit_time):  # 确保正常发送了时间信息再关闭窗口
            super().close()


class CustomDelegate(TableItemDelegate):
    signal_time_data = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.dialog = QDialog(parent)
        self.usm = Ui_Dialog()
        self.usm.setupUi(self.dialog)
        self.dialog.setWindowTitle('选择时间')

    def close(self):
        emit_time: str = self.ymd_hms()
        if self.signal_time_data.emit(emit_time):  # 确保正常发送了时间信息再关闭窗口
            self.dialog.close()

    def ymd_hms(self) -> str:
        ymd = self.usm.calendar_picker_ymd.getDate()
        hms = self.usm.time_picker_hms.getTime()
        year = ymd.year()
        month = ymd.month()
        day = ymd.day()
        hour = hms.hour()
        minute = hms.minute()
        second = hms.second()
        # 构造日期时间字符串
        formatted_string = f"{year}年{month}月{day}日 {hour:02}:{minute:02}:{second:02}"
        return formatted_string

    def createEditor(self, parent, option, index):
        if index.column() == 0:
            return None
        elif index.column() in range(1, 4):
            self.usm.push_button_ok.clicked.connect(self.close)
            self.dialog.exec_()
            return None


class APP(QMainWindow, Ui_MainWindow):
    software_name = 'File Date Changer'
    default_path = os.path.abspath(os.getcwd())

    def __init__(self):
        super(APP, self).__init__()
        self.file_name: list = []  # 存储路径->[路径]
        self.file_info: dict = {}  # 存储->{路径:[创建时间,修改时间,访问时间]}
        self.current_click_row: int = 0  # 初始化当前点击的行
        self.current_click_column: int = 0  # 初始化当前点击的列
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.delegate: CustomDelegate = ...  # 定义表格自定义委托

        self.setWindowTitle('文件日期修改器 By 雪碧(Gentlesprite)')
        self.setWindowIcon(QIcon(":/res/logo.ico"))

        self.init_table()  # 初始化表格内容
        self.band()

    def init_table(self):
        self.ui.table_widget_info_bar.setContextMenuPolicy(Qt.CustomContextMenu)
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

    def band(self):
        self.ui.push_button_change_time.clicked.connect(self.change_time)
        self.ui.table_widget_info_bar.customContextMenuRequested.connect(self.table_func_menu)
        self.ui.push_button_open_dir.clicked.connect(lambda: self.open_dir_mode(change_mode=UserFormChangeMode.new))
        self.ui.text_edit_path_input.signal_drop.connect(self.drop_mode)
        self.ui.text_edit_path_input.signal_paste.connect(self.paste_mode)
        self.ui.text_edit_path_input.textChanged.connect(
            lambda: self.typing_mode(self.ui.text_edit_path_input.toPlainText()))
        self.ui.table_widget_info_bar.itemClicked.connect(self.set_table)
        self.delegate.signal_time_data.connect(self.receive_time_data)
        self.ui.table_widget_info_bar.cellClicked.connect(self.get_clicked_roco)
        self.ui.table_widget_info_bar.itemEntered.connect(self.update_tooltip)

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

    def get_clicked_roco(self, row: int, column: int) -> None:  # 实时更新点击的行和列
        logger.debug(f'点击了第行:{row},列:{column}')
        self.current_click_row: int = row
        self.current_click_column: int = column
        if self.current_click_column == 0:
            self.open_dir_mode(change_mode=UserFormChangeMode.path)
        elif self.current_click_column in range(1, 3):
            ...

    def receive_time_data(self, new_time: str) -> None:  # 更新用户通过二级窗口手动选择的日期到表格中,并且更新到self.file_info字典
        # 通过当前点击行列数来获取当前第一列的路径数据
        self.set_table(change_mode=UserFormChangeMode.time, data=new_time)

    def receive_path_data(self, new_path: str) -> None:  #

        self.set_table(change_mode=UserFormChangeMode.time, data=new_path)

    def single_change_time(self, data):
        dialog = QDialog()
        usm = Ui_Dialog()
        usm.setupUi(dialog)
        dialog.setWindowTitle('选择时间')

        def close():
            usm.push_button_ok.clicked.connect(close)
            dialog.exec_()

    def table_func_menu(self, pos) -> None:
        row: int = self.ui.table_widget_info_bar.rowAt(pos.y())  # 获取当前右键的行
        column: int = self.ui.table_widget_info_bar.columnAt(pos.x())  # 获取当前右键的列
        path_data: tuple = (self.ui.table_widget_info_bar.item(row, 0).text(), row, column)
        create_data: tuple = (self.ui.table_widget_info_bar.item(row, 1).text(), row, column)
        modify_data: tuple = (self.ui.table_widget_info_bar.item(row, 2).text(), row, column)
        access_date: tuple = (self.ui.table_widget_info_bar.item(row, 3).text(), row, column)
        menu = RoundMenu()
        menu.addActions([QAction(
            FIF.CUT.icon(),
            self.tr('变更路径'),
            self,
            triggered=lambda: self.single_change_time(path_data)),
            QAction(
                FIF.CUT.icon(),
                self.tr('变更创建时间'),
                self,
                triggered=lambda: self.single_change_time(create_data)), QAction(
                FIF.CUT.icon(),
                self.tr('变更修改时间'),
                self,
                triggered=lambda: self.single_change_time(modify_data)), QAction(
                FIF.CUT.icon(),
                self.tr('变更访问时间'),
                self,
                triggered=lambda: self.single_change_time(access_date))]
        )
        menu.exec_(self.ui.table_widget_info_bar.mapToGlobal(pos))

    @staticmethod
    def get_file_time(file_path: str) -> list:
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
                self.ui.table_widget_info_bar.horizontalHeader().setSectionResizeMode(
                    QHeaderView.ResizeMode.ResizeToContents)
                self.ui.table_widget_info_bar.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
                self.ui.table_widget_info_bar.horizontalHeader().setMaximumSectionSize(200)  # 设置最大宽度为200像素
                # 滚动到新增的项
                self.file_info[file_path] = [create_time, modify_time, access_time]
                self.ui.table_widget_info_bar.scrollToItem(path_item)

    def set_table(self, change_mode: UserFormChangeMode = UserFormChangeMode.new,
                  **kwargs: Optional[str]) -> None:  # 增
        if change_mode == UserFormChangeMode.new:
            self._no_signal_change_text()
            self._process_new_table()
        elif change_mode == UserFormChangeMode.path:
            row = self.current_click_row
            column = self.current_click_column
            new_path: str = kwargs['data']
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
                        self.file_name.remove(old_key)
                        self.file_info[new_path] = [create_time, modify_time, access_time]
                        self.file_name.append(new_path)
                        break
                # 将字符串转换为Qtable对象
                create_time_item: QTableWidgetItem = QTableWidgetItem(create_time)
                modify_time_item: QTableWidgetItem = QTableWidgetItem(modify_time)
                access_time_item: QTableWidgetItem = QTableWidgetItem(access_time)
                new_path_item: QTableWidgetItem = QTableWidgetItem(new_path)
                self.ui.table_widget_info_bar.setItem(row, column, new_path_item)
                self.ui.table_widget_info_bar.setItem(row, 1, create_time_item)
                self.ui.table_widget_info_bar.setItem(row, 2, modify_time_item)
                self.ui.table_widget_info_bar.setItem(row, 3, access_time_item)
                logger.debug(f'已修改: {path} -> {new_path}')
                logger.debug(f'当前字典为{self.file_info},列表为{self.file_name}')
        elif change_mode == UserFormChangeMode.time:
            row = self.current_click_row
            column = self.current_click_column
            new_time: str = kwargs['data']
            path: str = self.ui.table_widget_info_bar.item(row, 0).text()
            match_value: list = self.file_info[path]
            logger.debug(f'找到路径:{path}对应的日期为:{match_value}')
            match_value[self.current_click_column - 1] = new_time  # 列数-1得到对应索引值[创建时间,修改时间,访问时间]
            logger.debug(f'当前更新的字典为:{self.file_info}')
            item_ymd = QTableWidgetItem(new_time)  # 转化为QTableWidgetItem对象
            self.ui.table_widget_info_bar.setItem(row, column, item_ymd)  # 更新到面板中

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
        else:
            logger.debug(f'要删除的内容 "{content_to_delete}" 未找到')

    def _get_all_items(self):  # 查
        # 获取行数和列数
        total_rows: int = self.ui.table_widget_info_bar.rowCount()  # 行
        total_columns: int = self.ui.table_widget_info_bar.columnCount()  # 列
        # 逐行获取每个项的内容
        all_items: list = []
        for row in range(total_rows):
            for column in range(total_columns):
                item: QTableWidgetItem = self.ui.table_widget_info_bar.item(row, column)
                if item is not None:
                    all_items.append(item.text())
        return all_items

    def _no_signal_change_text(self):
        self.ui.text_edit_path_input.textChanged.disconnect()
        self.ui.text_edit_path_input.setText('\n'.join(self.file_name) if self.file_name else '')
        self.ui.text_edit_path_input.textChanged.connect(
            lambda: self.typing_mode(self.ui.text_edit_path_input.toPlainText()))

    def open_dir_mode(self, change_mode=UserFormChangeMode.new):  # 打开文件夹模式
        # default_path = os.path.abspath(os.getcwd())
        default_path = 'D:\\2'
        if change_mode == UserFormChangeMode.new:
            data: list = [os.path.normpath(i) for i in
                          QFileDialog.getOpenFileNames(self, "选择文件", default_path, "All Files (*)")[
                              0]]
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
            new_key: str = QFileDialog.getOpenFileName(self, "选择文件", default_path, "All Files (*)")[0]
            self.set_table(change_mode=UserFormChangeMode.path, data=new_key)

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
        # 获取文本框中的内容
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

    def checker(func):
        def wrapper(self, *args, **kwargs):
            ymd = self.ui.calendar_picker_ymd.getDate()
            hms = self.ui.time_picker_hms.getTime()
            path: str = self.ui.text_edit_path_input.toPlainText().strip()  # 去除首尾空白字符

            # 用于显示错误消息的统一函数
            def show_error_message(message):
                MessageBox(title='提示', content=message, parent=self).show()

            if not path:
                show_error_message('内容为空!')
                return
            if ymd.isNull():
                show_error_message('未选择年月日!')
                return
            if hms.isNull():
                show_error_message('未选择时分秒!')
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
                    show_error_message('没有有效的路径。')
                    return
            # 执行原函数
            return func(self, *args, **kwargs)

        return wrapper

    @checker
    def change_time(self):
        logger.debug(f'所有文件路径{self.file_name},时间信息{self.file_info}')
        # self._set_file_time(file_name=total_file)
        #
        # Flyout.make(CustomFlyoutView(), self.ui.push_button_change_time, self,
        #             aniType=FlyoutAnimationType.DROP_DOWN)
        #
        # self.ui.table_widget_info_bar.clear()
        # self._no_signal_change_text()
        # self.file_name = []
        # self.file_info = {}

    def _set_file_time(self, file_name: list or str):
        if isinstance(file_name, list):
            for f in file_name:
                self.__set_file_time(f)
        elif isinstance(file_name, str):
            self.__set_file_time(file_name)

    def __set_file_time(self, file_name: str):
        ymd = self.ui.calendar_picker_ymd.getDate()
        hms = self.ui.time_picker_hms.getTime()
        year, month, day = ymd.year(), ymd.month(), ymd.day()
        hour, minute, second = hms.hour(), hms.minute(), hms.second()
        change_date_time = datetime(year, month, day, hour, minute, second)  # 文件的修改日期
        change_time_stamp = change_date_time.timestamp()  # 文件的修改日期的时间戳
        logger.debug(f'设定的时间为:{change_date_time} 时间戳为:{change_time_stamp}')
        res = APP.modifyFileTime(filePath=file_name, createTime=change_time_stamp, modifyTime=change_time_stamp,
                                 accessTime=change_time_stamp)
        if res == 0:
            logger.debug('修改完成')
        else:
            logger.error(res)

    @staticmethod
    def modifyFileTime(filePath, createTime, modifyTime, accessTime):
        """
        用来修改任意文件的相关时间属性，时间格式：时间戳
        :param filePath: 文件路径名
        :param createTime: 创建时间（时间戳）
        :param modifyTime: 修改时间（时间戳）
        :param accessTime: 访问时间（时间戳）
        :param offset: 时间偏移的秒数，tuple格式，顺序和参数时间对应
        """
        try:
            fh = CreateFile(filePath, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)
            create_time = datetime.fromtimestamp(createTime)
            access_time = datetime.fromtimestamp(accessTime)
            modify_time = datetime.fromtimestamp(modifyTime)
            SetFileTime(fh, create_time, access_time, modify_time)
            CloseHandle(fh)
            return 0
        except Exception as e:
            return e

    @staticmethod
    def setDpiFromWindowsSettings():
        """
        根据windows的DPI缩放来适配软件的DPI
        :return:
        """
        QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)


class CustomFlyoutView(FlyoutViewBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.label = BodyLabel(
            '设置成功')
        self.button = PrimaryPushButton('确定')
        self.button.clicked.connect(self.close)
        self.button.setFixedWidth(140)
        self.vBoxLayout.setSpacing(12)
        self.vBoxLayout.setContentsMargins(20, 16, 20, 16)
        self.vBoxLayout.addWidget(self.label)
        self.vBoxLayout.addWidget(self.button)


if __name__ == "__main__":
    APP.setDpiFromWindowsSettings()
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load(QLocale.system(), ":/lan/qfluentwidgets_")
    app.installTranslator(translator)
    w = APP()
    w.show()
    sys.exit(app.exec_())
