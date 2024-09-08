# -*- coding: utf-8 -*-
import os.path

################################################################################
## Form generated from reading UI file '2HYBGYR.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import CalendarPicker
from qfluentwidgets import TimePicker
from qfluentwidgets import LineEdit
from qfluentwidgets import ListWidget
from qfluentwidgets import VerticalPipsPager
from qfluentwidgets import LineEditMenu
from qfluentwidgets import Action


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(505, 222)
        Form.setMinimumSize(QSize(505, 222))
        Form.setMaximumSize(QSize(505, 222))
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_side = QHBoxLayout()
        self.input_side.setObjectName(u"input_side")
        self.lineEdit_path_text = NewQLineEdit(Form)
        self.lineEdit_path_text.setObjectName(u"lineEdit_path_text")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_path_text.sizePolicy().hasHeightForWidth())
        self.lineEdit_path_text.setSizePolicy(sizePolicy)
        self.lineEdit_path_text.setMinimumSize(QSize(380, 30))
        self.lineEdit_path_text.setMaximumSize(QSize(380, 30))

        self.input_side.addWidget(self.lineEdit_path_text)

        self.splitter = QSplitter(Form)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.VerticalPipsPager = VerticalPipsPager(self.splitter)
        QListWidgetItem(self.VerticalPipsPager)
        QListWidgetItem(self.VerticalPipsPager)
        QListWidgetItem(self.VerticalPipsPager)
        QListWidgetItem(self.VerticalPipsPager)
        QListWidgetItem(self.VerticalPipsPager)
        self.VerticalPipsPager.setObjectName(u"VerticalPipsPager")
        self.VerticalPipsPager.setMinimumSize(QSize(12, 5))
        self.VerticalPipsPager.setMaximumSize(QSize(12, 5))
        self.splitter.addWidget(self.VerticalPipsPager)
        self.push_button_open_dir = PushButton(self.splitter)
        self.push_button_open_dir.setObjectName(u"push_button_open_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.push_button_open_dir.sizePolicy().hasHeightForWidth())
        self.push_button_open_dir.setSizePolicy(sizePolicy1)
        self.push_button_open_dir.setMinimumSize(QSize(20, 20))
        self.push_button_open_dir.setMaximumSize(QSize(20, 20))
        self.splitter.addWidget(self.push_button_open_dir)

        self.input_side.addWidget(self.splitter)

        self.push_button_change_time = PushButton(Form)
        self.push_button_change_time.setObjectName(u"push_button_change_time")
        self.push_button_change_time.setMinimumSize(QSize(70, 30))
        self.push_button_change_time.setMaximumSize(QSize(80, 30))

        self.input_side.addWidget(self.push_button_change_time)

        self.verticalLayout.addLayout(self.input_side)

        self.time_side = QHBoxLayout()
        self.time_side.setObjectName(u"time_side")
        self.calendar_picker_ymd = CalendarPicker(Form)
        self.calendar_picker_ymd.setObjectName(u"calendar_picker_ymd")

        self.time_side.addWidget(self.calendar_picker_ymd)

        self.time_picker_hms = TimePicker(Form)
        self.time_picker_hms.setObjectName(u"time_picker_hms")
        self.time_picker_hms.setEnabled(True)
        self.time_picker_hms.setFocusPolicy(Qt.StrongFocus)
        self.time_picker_hms.setStyleSheet(u"ScrollButton {\n"
                                           "    background-color: rgb(249, 249, 249);\n"
                                           "    border: none;\n"
                                           "    border-radius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "CycleListWidget {\n"
                                           "    background-color: transparent;\n"
                                           "    border: none;\n"
                                           "    border-top-left-radius: 7px;\n"
                                           "    border-top-right-radius: 7px;\n"
                                           "    outline: none;\n"
                                           "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                           "}\n"
                                           "\n"
                                           "CycleListWidget::item {\n"
                                           "    color: black;\n"
                                           "    background-color: transparent;\n"
                                           "    border: none;\n"
                                           "    border-radius: 5px;\n"
                                           "    margin: 0 4px;\n"
                                           "    padding-left: 11px;\n"
                                           "    padding-right: 11px;\n"
                                           "}\n"
                                           "\n"
                                           "CycleListWidget::item:hover {\n"
                                           "    background-color: rgba(0, 0, 0, 9);\n"
                                           "}\n"
                                           "\n"
                                           "CycleListWidget::item:selected {\n"
                                           "    background-color: rgba(0, 0, 0, 9);\n"
                                           "}\n"
                                           "\n"
                                           "CycleListWidget::item:selected:active {\n"
                                           "    background-color: rgba(0, 0, 0, 6);\n"
                                           "}\n"
                                           "\n"
                                           "PickerPanel > #view {\n"
                                           "    background-color: rgb(249, 249, 249);\n"
                                           "    border: 1px solid rgba(0, 0, 0, 0.14);\n"
                                           "    border-ra"
                                           "dius: 7px;\n"
                                           "}\n"
                                           "\n"
                                           "SeparatorWidget {\n"
                                           "    background-color: rgb(234, 234, 234);\n"
                                           "}\n"
                                           "\n"
                                           "ItemMaskWidget {\n"
                                           "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                           "}\n"
                                           "\n"
                                           "PickerBase {\n"
                                           "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                           "    background: rgba(255, 255, 255, 0.7);\n"
                                           "    border: 1px solid rgba(0, 0, 0, 0.073);\n"
                                           "    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
                                           "    border-radius: 5px;\n"
                                           "    outline: none;\n"
                                           "}\n"
                                           "\n"
                                           "PickerBase:hover {\n"
                                           "    background: rgba(249, 249, 249, 0.5);\n"
                                           "}\n"
                                           "\n"
                                           "PickerBase:pressed {\n"
                                           "    background: rgba(249, 249, 249, 0.3);\n"
                                           "    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
                                           "}\n"
                                           "\n"
                                           "PickerBase:disabled {\n"
                                           "    color: rgba(0, 0, 0, 0.36);\n"
                                           "    background: rgba(255, 255, 255, 0.3);\n"
                                           "    border: 1px solid rgba(0, 0, 0, 0.06);\n"
                                           "    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton {\n"
                                           "    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
                                           "    colo"
                                           "r: rgba(0, 0, 0, 0.6);\n"
                                           "    background-color: transparent;\n"
                                           "    border: none;\n"
                                           "    outline: none;\n"
                                           "    padding-left: 10px;\n"
                                           "    padding-right: 10px;\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton:disabled {\n"
                                           "    color: rgba(0, 0, 0, 0.36);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[hasBorder=true]:enabled {\n"
                                           "    border-right: 1px solid rgba(0, 0, 0, 0.073);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[hasBorder=true]:disabled {\n"
                                           "    border-right: 1px solid rgba(0, 0, 0, 0.06);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[hasBorder=false] {\n"
                                           "    border-right: transparent;\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[enter=true]:enabled {\n"
                                           "    color: rgba(0, 0, 0, 0.896);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[hasValue=true]:enabled{\n"
                                           "    color: rgb(0, 0, 0);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[pressed=true] {\n"
                                           "    color: rgba(0, 0, 0, 0.6);\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[align=\"center\"] {\n"
                                           "    text-align: center;\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[align=\"left\"] {\n"
                                           "    text-align: left;\n"
                                           "}\n"
                                           "\n"
                                           "#pickerButton[align=\"right\"] {\n"
                                           "    text-align: right;\n"
                                           "}\n"
                                           "")
        self.time_picker_hms.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.time_picker_hms.setAutoDefault(False)
        self.time_picker_hms.setFlat(False)
        self.time_picker_hms.setSecondVisible(True)

        self.time_side.addWidget(self.time_picker_hms)

        self.verticalLayout.addLayout(self.time_side)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.list_widget_info_bar = ListWidget(Form)
        self.list_widget_info_bar.setObjectName(u"list_widget_info_bar")
        self.list_widget_info_bar.setMinimumSize(QSize(485, 131))
        self.list_widget_info_bar.setMaximumSize(QSize(485, 131))

        self.verticalLayout_2.addWidget(self.list_widget_info_bar)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Form)

        self.time_picker_hms.setDefault(False)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit_path_text.setText("")

        __sortingEnabled = self.VerticalPipsPager.isSortingEnabled()
        self.VerticalPipsPager.setSortingEnabled(False)
        self.VerticalPipsPager.setSortingEnabled(__sortingEnabled)

        self.push_button_open_dir.setText(QCoreApplication.translate("Form", u"\u00b7\u00b7", None))
        self.push_button_change_time.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
        # if QT_CONFIG(tooltip)
        self.time_picker_hms.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.time_picker_hms.setText("")
    # retranslateUi





class NewQLineEdit(LineEdit):  # 新建类，命名为 `NewQLineEdit`
    signal = Signal(list)

    def __init__(self, *args, **kwargs):  # 继承父类构造函数
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)  # 设置接受拖放动作

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 当文件拖入此区域时为True
            event.accept()  # 接受拖入文件
        else:
            event.ignore()  # 忽略拖入或关闭

    def dropEvent(self, event):  # 本方法为父类方法，本方法中的event为鼠标放事件对象
        urls = [u for u in event.mimeData().urls()]  # 范围文件路径的Qt内部类型对象列表，由于支持多个文件同时拖入所以使用列表存放
        path: list = []
        for url in urls:
            if url not in path:
                path.append(os.path.normpath(url.path()[1:]))
        current_content: str = self.text()
        if current_content:
            content = current_content.split('&')
            for i in content:
                if i.strip():  # 确保去除空白后的项不为空
                    if i not in path:
                        path.append(i.strip())  # 添加到路径列表中
        self.signal.emit(path)

    def paste(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        print(mime_data)
        if mime_data.hasUrls():
            file_urls = mime_data.urls()
            file_paths = [url.toLocalFile() for url in file_urls]
            formatted_paths = "&".join(file_paths)
            self.setText(formatted_paths + '&')

        else:
            super().paste()

    def keyPressEvent(self, event):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if event.matches(QKeySequence.Paste) and mime_data.hasUrls():
            # 执行你的操作
            print("Ctrl+V 被按下")
            if mime_data.hasUrls():
                self.paste()
        else:
            super().keyPressEvent(event)
