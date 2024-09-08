# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/7 19:24
# File:app

import sys
import os
from PySide6.QtCore import Qt, QLocale, QTranslator
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFileDialog, QListWidgetItem
from qfluentwidgets import Flyout, FlyoutViewBase, BodyLabel, PrimaryPushButton, FlyoutAnimationType
from qfluentwidgets.components.dialog_box import MessageBox
from loguru import logger
import res_rc
from ui import Ui_Form, QFrame
from datetime import datetime
# import time
from win32file import CreateFile, SetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
import win32timezone

logger.add(
    os.path.join(os.getcwd(), "pb.log"),
    rotation="10 MB",
    retention="10 days",
    level="DEBUG",
)


class APP(QFrame, Ui_Form):
    software_name = 'File Date Changer'

    def __init__(self):
        super(APP, self).__init__()
        self.file_name: list = []
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":res/logo.ico"))
        self.setWindowTitle('文件日期修改器 By 雪碧(Gentlesprite)')
        self.ui.list_widget_info_bar.setContextMenuPolicy(Qt.CustomContextMenu)
        self.band()

    def band(self):
        self.ui.push_button_change_time.clicked.connect(self.change_time)
        self.ui.list_widget_info_bar.itemClicked.connect(self.delete_this)
        self.ui.list_widget_info_bar.customContextMenuRequested.connect(self.change_single_time)
        self.ui.push_button_open_dir.clicked.connect(self.open_dir_mode)
        self.ui.lineEdit_path_text.signal.connect(self.drag_mode)
        self.ui.lineEdit_path_text.textChanged.connect(self.typing_mode)


    def change_single_time(self):

        print('鼠标右键单击')

    def _add_info_bar(self) -> None:  # 增
        all_items: list = self._get_all_items()  # 获取所有项的内容
        logger.debug(all_items)
        for i in self.file_name:
            if i not in all_items:
                item = QListWidgetItem(i)
                self.ui.list_widget_info_bar.addItem(item)
                self.ui.list_widget_info_bar.scrollToItem(item)
        return None

    def delete_content(self, content_to_delete: str):  # 删除对应内容的项
        # 查找需要删除的项的索引
        index = -1
        for i in range(self.ui.list_widget_info_bar.count()):
            item = self.ui.list_widget_info_bar.item(i)
            if item.text() == content_to_delete:
                index = i
                break
        if index != -1:
            # 删除列表中的项
            self.ui.list_widget_info_bar.takeItem(index)
            logger.debug(f'已删除: {content_to_delete}')
            # 从文件名列表中也移除
            self.file_name.remove(content_to_delete)
        else:
            logger.debug(f'要删除的内容 "{content_to_delete}" 未找到')

    def delete_this(self, path: QListWidgetItem):  # 删
        index = self.ui.list_widget_info_bar.row(path)  # 获取点击的索引
        self.ui.list_widget_info_bar.takeItem(index)  # 删除该索引的内容
        content: str = path.text()  # 获取该索引的内容
        logger.debug(f'已删除:{content}')
        self.file_name.remove(content)  # 从列表里也移除
        self.ui.lineEdit_path_text.textChanged.disconnect(self.typing_mode)  # 首先断开信号槽避免执行text_change
        self.ui.lineEdit_path_text.setText(
            '&'.join(self.file_name)) if self.file_name else self.ui.lineEdit_path_text.clear()  # 最后重新设定到输入框中
        self.ui.lineEdit_path_text.textChanged.connect(self.typing_mode)  # 再重新打开信号槽

    def _get_all_items(self):  # 查
        # 获取项的总数
        total_items = self.ui.list_widget_info_bar.count()
        # 逐个获取每个项的内容
        all_items = []
        for i in range(total_items):
            item = self.ui.list_widget_info_bar.item(i)
            if item is not None:
                all_items.append(item.text())
        return all_items

    def open_dir_mode(self):  # 打开文件夹模式
        path = os.path.abspath(os.getcwd())
        res: list = [os.path.normpath(i) for i in
                     QFileDialog.getOpenFileNames(self, "选择文件", path, "All Files (*)")[0]]
        if self.file_name:
            for i in res:
                if i.lower() not in [f.lower() for f in self.file_name]:
                    self.file_name.append(i)
                else:
                    logger.warning(f'{i}已存在!')
        else:
            self.file_name = res
        # 打开文件后未选择路径去重/
        self.ui.lineEdit_path_text.textChanged.disconnect(self.typing_mode)  # 首先断开信号槽避免执行text_change
        # self.ui.lineEdit_path_text.setText('&'.join(self.file_name)) if self.file_name else 0
        self.ui.lineEdit_path_text.setText('&'.join(self.file_name) + '&' if self.file_name else '')
        self._add_info_bar()
        self.ui.lineEdit_path_text.textChanged.connect(self.typing_mode)  # 再重新打开信号槽

    def drag_mode(self, value):  # 拖入模式
        for i in value:
            if i.lower() not in [f.lower() for f in self.file_name]:
                self.file_name.append(i)
        logger.debug(self.file_name)
        self.ui.lineEdit_path_text.textChanged.disconnect(self.typing_mode)  # 首先断开信号槽避免执行text_change
        self.ui.lineEdit_path_text.setText('&'.join(self.file_name) + '&' if self.file_name else '')  # 最后重新设定到输入框中
        self.ui.lineEdit_path_text.textChanged.connect(self.typing_mode)  # 再重新打开信号槽
        self._add_info_bar()

    def typing_mode(self, res):
        # 获取文本框中的内容
        # 检查用户是否完成了输入
        file_names = res.rstrip('&').split('&')
        if res and res.endswith('&'):
            # 以 '&' 分隔文本
            # 遍历分隔后的文件名
            for file_name in file_names:
                # 去除首尾空白字符
                file_name = file_name.strip()

                # 如果文件名存在，并且不在列表中，则添加到列表中
                if file_name and os.path.exists(file_name) and file_name.lower() not in [f.lower() for f in
                                                                                         self.file_name]:
                    self.file_name.append(file_name)
            # 存储路径
            self._add_info_bar()
            logger.debug(f'手动输入内容发生改变:{self.file_name}')
        else:
            need_remove = [f for f in self.file_name if f not in file_names]
            for item in need_remove:
                self.delete_content(item)
            self._add_info_bar()

    def checker(func):
        def wrapper(self, *args, **kwargs):
            ymd = self.ui.calendar_picker_ymd.getDate()
            hms = self.ui.time_picker_hms.getTime()
            path: str = self.ui.lineEdit_path_text.text().strip()  # 去除首尾空白字符

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
            if not path.endswith('&') and os.path.exists(path):
                # 如果是有效路径，则在末尾添加'&'
                new_path = path + '&'
                logger.warning(f'路径没有以&结尾,已自动添加:{new_path}')
                self.ui.lineEdit_path_text.setText(new_path)
            elif not path.endswith('&'):
                # 处理多路径情况
                res = path.rstrip('&').split('&')
                valid_paths = []
                for i in res:
                    if os.path.exists(i):
                        valid_paths.append(i + '&')
                        logger.debug(f'有效路径:{i}&')
                    else:
                        logger.warning(f'路径不存在:{i}')
                if valid_paths:
                    # 如果有有效路径，则将它们拼接起来
                    new_path = ''.join(valid_paths)
                    self.ui.lineEdit_path_text.setText(new_path)
                else:
                    # 如果没有有效路径，则不执行原函数
                    show_error_message('没有有效的路径。')
                    return
            # 执行原函数
            return func(self, *args, **kwargs)

        return wrapper

    @checker
    def change_time(self):
        file: list = [os.path.normpath(f) for f in self.file_name if os.path.isfile(f)]
        folder_file: list = [os.path.normpath(f) for f in self.file_name if os.path.isdir(f)]
        lst_folder_file: list = [os.path.join(i, f) for i in folder_file for f in os.listdir(i) if
                                 os.path.isfile(os.path.join(i, f))]
        total_file: list = list(set(file + lst_folder_file))
        self._set_file_time(file_name=total_file)

        Flyout.make(CustomFlyoutView(), self.ui.push_button_change_time, self,
                    aniType=FlyoutAnimationType.DROP_DOWN)

        self.ui.list_widget_info_bar.clear()
        self.ui.lineEdit_path_text.textChanged.disconnect(self.typing_mode)
        self.ui.lineEdit_path_text.clear()
        self.ui.lineEdit_path_text.textChanged.connect(self.typing_mode)
        self.file_name = []

        logger.debug(f'文件有:{file}\n文件夹有:{folder_file},其中包含了:{lst_folder_file}\n总文件:{total_file}')

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


def setDpiFromWindowsSettings():
    """
    根据windows的DPI缩放来适配软件的DPI
    :return:
    """
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)


if __name__ == "__main__":
    setDpiFromWindowsSettings()
    app = QApplication(sys.argv)
    translator = QTranslator()
    translator.load(QLocale.system(), ":/lan/qfluentwidgets_")
    app.installTranslator(translator)
    w = APP()
    w.show()
    sys.exit(app.exec_())
