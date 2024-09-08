# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/15 15:53
# File:ui
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app0nQdZPN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from qfluentwidgets import CheckBox
from qfluentwidgets import PushButton
from qfluentwidgets import ToolButton
from qfluentwidgets import CalendarPicker
from qfluentwidgets import TimePicker
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import TextEdit
from qfluentwidgets import TableWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 389)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.table_widget_info_bar = TableWidget(self.centralwidget)
        self.table_widget_info_bar.setObjectName(u"table_widget_info_bar")

        self.gridLayout_4.addWidget(self.table_widget_info_bar, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.text_edit_path_input = DropTextEdit(self.centralwidget)
        self.text_edit_path_input.setObjectName(u"text_edit_path_input")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_edit_path_input.sizePolicy().hasHeightForWidth())
        self.text_edit_path_input.setSizePolicy(sizePolicy)
        self.text_edit_path_input.setMinimumSize(QSize(500, 140))

        self.gridLayout_3.addWidget(self.text_edit_path_input, 0, 0, 3, 1)

        self.StrongBodyLabel = StrongBodyLabel(self.centralwidget)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setMinimumSize(QSize(90, 20))
        self.StrongBodyLabel.setMaximumSize(QSize(90, 20))

        self.gridLayout_3.addWidget(self.StrongBodyLabel, 0, 2, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.time_picker_hms = TimePicker(self.centralwidget)
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

        self.verticalLayout.addWidget(self.time_picker_hms)

        self.calendar_picker_ymd = CalendarPicker(self.centralwidget)
        self.calendar_picker_ymd.setObjectName(u"calendar_picker_ymd")
        self.calendar_picker_ymd.setMinimumSize(QSize(240, 30))
        self.calendar_picker_ymd.setMaximumSize(QSize(240, 30))
        self.calendar_picker_ymd.setAutoDefault(False)

        self.verticalLayout.addWidget(self.calendar_picker_ymd)

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.check_box_modify_time = CheckBox(self.centralwidget)
        self.check_box_modify_time.setObjectName(u"check_box_modify_time")
        self.check_box_modify_time.setMinimumSize(QSize(29, 22))
        self.check_box_modify_time.setMaximumSize(QSize(90, 20))
        self.check_box_modify_time.setChecked(True)

        self.gridLayout.addWidget(self.check_box_modify_time, 0, 0, 1, 1)

        self.check_box_create_time = CheckBox(self.centralwidget)
        self.check_box_create_time.setObjectName(u"check_box_create_time")
        self.check_box_create_time.setMinimumSize(QSize(29, 22))
        self.check_box_create_time.setMaximumSize(QSize(90, 20))
        self.check_box_create_time.setChecked(True)

        self.gridLayout.addWidget(self.check_box_create_time, 1, 0, 1, 1)

        self.check_box_access_time = CheckBox(self.centralwidget)
        self.check_box_access_time.setObjectName(u"check_box_access_time")
        self.check_box_access_time.setMinimumSize(QSize(29, 22))
        self.check_box_access_time.setMaximumSize(QSize(90, 20))
        self.check_box_access_time.setChecked(True)

        self.gridLayout.addWidget(self.check_box_access_time, 2, 0, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 2, 1, 1)

        self.tool_button_open_dir = ToolButton(self.centralwidget)
        self.tool_button_open_dir.setObjectName(u"tool_button_open_dir")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tool_button_open_dir.sizePolicy().hasHeightForWidth())
        self.tool_button_open_dir.setSizePolicy(sizePolicy1)
        self.tool_button_open_dir.setMinimumSize(QSize(30, 30))
        self.tool_button_open_dir.setMaximumSize(QSize(30, 30))

        self.gridLayout_3.addWidget(self.tool_button_open_dir, 2, 1, 1, 1)

        self.push_button_change_time = PushButton(self.centralwidget)
        self.push_button_change_time.setObjectName(u"push_button_change_time")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.push_button_change_time.sizePolicy().hasHeightForWidth())
        self.push_button_change_time.setSizePolicy(sizePolicy2)
        self.push_button_change_time.setMinimumSize(QSize(335, 30))
        self.push_button_change_time.setMaximumSize(QSize(335, 30))

        self.gridLayout_3.addWidget(self.push_button_change_time, 2, 2, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayout_3.setColumnMinimumWidth(0, 2)
        self.gridLayout_3.setColumnMinimumWidth(1, 1)
        self.gridLayout_3.setColumnMinimumWidth(2, 2)
        self.gridLayout_3.setRowMinimumHeight(0, 2)
        self.gridLayout_3.setRowMinimumHeight(1, 1)
        self.gridLayout_3.setRowMinimumHeight(2, 2)

        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.time_picker_hms.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.StrongBodyLabel.setText(
            QCoreApplication.translate("MainWindow", u"\u8bbe\u5b9a\u5168\u5c40\u65e5\u671f", None))
        # if QT_CONFIG(tooltip)
        self.time_picker_hms.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.time_picker_hms.setText("")
        self.check_box_modify_time.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u65f6\u95f4", None))
        self.check_box_create_time.setText(QCoreApplication.translate("MainWindow", u"\u521b\u5efa\u65f6\u95f4", None))
        self.check_box_access_time.setText(QCoreApplication.translate("MainWindow", u"\u8bbf\u95ee\u65f6\u95f4", None))
        self.push_button_change_time.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
    # retranslateUi


class DropTextEdit(TextEdit):  # 新建类，命名为 `NewQLineEdit`
    signal_drop = Signal(list)
    signal_paste = Signal(list)

    def __init__(self, *args, **kwargs):  # 继承父类构造函数
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)  # 设置接受拖放动作
        self.setWordWrapMode(QTextOption.NoWrap)  # 禁用自动换行

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():  # 当文件拖入此区域时为True
            event.accept()  # 接受拖入文件
        else:
            event.ignore()  # 忽略拖入或关闭

    def dropEvent(self, event):
        # 获取拖放事件中的URL列表，转换成本地文件路径格式
        urls = [u.toLocalFile() for u in event.mimeData().urls()]
        # 从URL中提取文件路径，过滤掉文件夹路径
        paths = [os.path.normpath(url) for url in urls if os.path.isfile(os.path.normpath(url))]
        # 将文本框中的文件路径添加到路径列表中，过滤掉重复项
        current_content = self.toPlainText()
        if current_content:
            paths.extend(os.path.normpath(line.strip()) for line in current_content.split('\n') if
                         line.strip() and os.path.isfile(line.strip()))
        # 发送信号，传递路径列表
        self.signal_drop.emit(paths)

    def paste(self):
        clipboard = QApplication.clipboard()
        mime_data = clipboard.mimeData()
        if mime_data.hasUrls():
            file_urls = mime_data.urls()
            # file_paths = [url.toLocalFile() for url in file_urls]
            file_paths = [os.path.normpath(url.toLocalFile()) for url in file_urls]
            expected_dir = [i for i in file_paths if os.path.isfile(i)]
            current_content = self.toPlainText()
            if current_content:
                expected_dir.extend(os.path.normpath(line.strip()) for line in current_content.split('\n') if
                                    line.strip() and os.path.isfile(line.strip()))
            # formatted_paths = "\n".join(expected_dir)
            # self.setText(formatted_paths+'\n')
            self.signal_paste.emit(expected_dir)
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
