# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/15 15:53
# File:ui
# -*- coding: utf-8 -*-
################################################################################
## Form generated from reading UI file 'app0LgiTin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import os
from qfluentwidgets import CheckBox
from qfluentwidgets import PushButton
from qfluentwidgets import ToolButton
from qfluentwidgets import CalendarPicker
from qfluentwidgets import TimePicker
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import TextEdit
from qfluentwidgets import TableWidget



class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(898, 352)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(898, 0))
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.table_widget_info_bar = TableWidget(Form)
        self.table_widget_info_bar.setObjectName(u"table_widget_info_bar")

        self.gridLayout_2.addWidget(self.table_widget_info_bar, 0, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.text_edit_path_input = DropTextEdit(Form)
        self.text_edit_path_input.setObjectName(u"text_edit_path_input")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_edit_path_input.sizePolicy().hasHeightForWidth())
        self.text_edit_path_input.setSizePolicy(sizePolicy1)
        self.text_edit_path_input.setMinimumSize(QSize(500, 124))
        self.text_edit_path_input.setMaximumSize(QSize(16777215, 124))

        self.horizontalLayout_3.addWidget(self.text_edit_path_input)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.StrongBodyLabel = StrongBodyLabel(Form)
        self.StrongBodyLabel.setObjectName(u"StrongBodyLabel")
        self.StrongBodyLabel.setMinimumSize(QSize(90, 20))
        self.StrongBodyLabel.setMaximumSize(QSize(90, 20))

        self.horizontalLayout_2.addWidget(self.StrongBodyLabel)

        self.tool_button_toggle_theme = ToolButton(Form)
        self.tool_button_toggle_theme.setObjectName(u"tool_button_toggle_theme")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tool_button_toggle_theme.sizePolicy().hasHeightForWidth())
        self.tool_button_toggle_theme.setSizePolicy(sizePolicy2)
        self.tool_button_toggle_theme.setMinimumSize(QSize(20, 20))
        self.tool_button_toggle_theme.setMaximumSize(QSize(20, 20))
        self.tool_button_toggle_theme.setStyleSheet(u"PushButton, ToolButton, ToggleButton, ToggleToolButton {\n"
"    color: black;\n"
"    background: rgba(255, 255, 255, 0.7);\n"
"    border: 1px solid rgba(0, 0, 0, 0.073);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"    border-radius: 5px;\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 5px 12px 6px 12px;\n"
"    outline: none;\n"
"}\n"
"\n"
"ToolButton {\n"
"    padding: 5px 9px 6px 8px;\n"
"}\n"
"\n"
"PushButton[hasIcon=false] {\n"
"    padding: 5px 12px 6px 12px;\n"
"}\n"
"\n"
"PushButton[hasIcon=true] {\n"
"    padding: 5px 12px 6px 36px;\n"
"}\n"
"\n"
"DropDownToolButton, PrimaryDropDownToolButton {\n"
"    padding: 5px 31px 6px 8px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=false],\n"
"PrimaryDropDownPushButton[hasIcon=false] {\n"
"    padding: 5px 31px 6px 12px;\n"
"}\n"
"\n"
"DropDownPushButton[hasIcon=true],\n"
"PrimaryDropDownPushButton[hasIcon=true] {\n"
"    padding: 5px 31px 6px 36px;\n"
"}\n"
"\n"
"PushButton:hover, ToolButton:hover, ToggleButton:hover, To"
                        "ggleToolButton:hover {\n"
"    background: rgba(249, 249, 249, 0.5);\n"
"}\n"
"\n"
"PushButton:pressed, ToolButton:pressed, ToggleButton:pressed, ToggleToolButton:pressed {\n"
"    color: rgba(0, 0, 0, 0.63);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.073);\n"
"}\n"
"\n"
"PushButton:disabled, ToolButton:disabled, ToggleButton:disabled, ToggleToolButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.36);\n"
"    background: rgba(249, 249, 249, 0.3);\n"
"    border: 1px solid rgba(0, 0, 0, 0.06);\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.06);\n"
"}\n"
"\n"
"\n"
"PrimaryPushButton,\n"
"PrimaryToolButton,\n"
"ToggleButton:checked,\n"
"ToggleToolButton:checked {\n"
"    color: white;\n"
"    background-color: #009faa;\n"
"    border: 1px solid #00a7b3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:hover,\n"
"PrimaryToolButton:hover,\n"
"ToggleButton:checked:hover,\n"
"ToggleToolButton:checked:hover {\n"
"    background-color: #00a7b3"
                        ";\n"
"    border: 1px solid #2daab3;\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"PrimaryPushButton:pressed,\n"
"PrimaryToolButton:pressed,\n"
"ToggleButton:checked:pressed,\n"
"ToggleToolButton:checked:pressed {\n"
"    color: rgba(255, 255, 255, 0.63);\n"
"    background-color: #3eabb3;\n"
"    border: 1px solid #3eabb3;\n"
"}\n"
"\n"
"PrimaryPushButton:disabled,\n"
"PrimaryToolButton:disabled,\n"
"ToggleButton:checked:disabled,\n"
"ToggleToolButton:checked:disabled {\n"
"    color: rgba(255, 255, 255, 0.9);\n"
"    background-color: rgb(205, 205, 205);\n"
"    border: 1px solid rgb(205, 205, 205);\n"
"}\n"
"\n"
"SplitDropButton,\n"
"PrimarySplitDropButton {\n"
"    border-left: none;\n"
"    border-top-left-radius: 0;\n"
"    border-bottom-left-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton,\n"
"#splitToolButton,\n"
"#primarySplitPushButton,\n"
"#primarySplitToolButton {\n"
"    border-top-right-radius: 0;\n"
"    border-bottom-right-radius: 0;\n"
"}\n"
"\n"
"#splitPushButton:pressed,\n"
"#splitTool"
                        "Button:pressed,\n"
"SplitDropButton:pressed {\n"
"    border-bottom: 1px solid rgba(0, 0, 0, 0.183);\n"
"}\n"
"\n"
"PrimarySplitDropButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"#primarySplitPushButton, #primarySplitToolButton {\n"
"    border-right: 1px solid #3eabb3;\n"
"}\n"
"\n"
"#primarySplitPushButton:pressed, #primarySplitToolButton:pressed {\n"
"    border-bottom: 1px solid #007780;\n"
"}\n"
"\n"
"HyperlinkButton {\n"
"    /* font: 14px 'Segoe UI', 'Microsoft YaHei'; */\n"
"    padding: 6px 12px 6px 12px;\n"
"    color: #009faa;\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=false] {\n"
"    padding: 6px 12px 6px 12px;\n"
"}\n"
"\n"
"HyperlinkButton[hasIcon=true] {\n"
"    padding: 6px 12px 6px 36px;\n"
"}\n"
"\n"
"HyperlinkButton:hover {\n"
"    color: #009faa;\n"
"    background-color: rgba(0, 0, 0, 10);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:pressed {\n"
"    color: #009faa;\n"
""
                        "    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"HyperlinkButton:disabled {\n"
"    color: rgba(0, 0, 0, 0.43);\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"RadioButton {\n"
"    min-height: 24px;\n"
"    max-height: 24px;\n"
"    background-color: transparent;\n"
"    font: 14px 'Segoe UI', 'Microsoft YaHei', 'PingFang SC';\n"
"    color: black;\n"
"}\n"
"\n"
"RadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 11px;\n"
"    border: 2px solid #999999;\n"
"    background-color: rgba(0, 0, 0, 5);\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"RadioButton::indicator:hover {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"\n"
"RadioButton::indicator:pressed {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(225, 2"
                        "24, 223),\n"
"            stop:1 rgb(225, 224, 223));\n"
"}\n"
"\n"
"RadioButton::indicator:checked {\n"
"    height: 22px;\n"
"    width: 22px;\n"
"    border: none;\n"
"    border-radius: 11px;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.6 rgb(255, 255, 255),\n"
"            stop:0.7 #009faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton::indicator:checked:pressed {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 #0"
                        "09faa,\n"
"            stop:1 #009faa);\n"
"}\n"
"\n"
"RadioButton:disabled {\n"
"    color: rgba(0, 0, 0, 110);\n"
"}\n"
"\n"
"RadioButton::indicator:disabled {\n"
"    border: 2px solid #bbbbbb;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"RadioButton::indicator:disabled:checked {\n"
"    border: none;\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5,\n"
"            stop:0 rgb(255, 255, 255),\n"
"            stop:0.5 rgb(255, 255, 255),\n"
"            stop:0.6 rgba(0, 0, 0, 0.2169),\n"
"            stop:1 rgba(0, 0, 0, 0.2169));\n"
"}\n"
"\n"
"TransparentToolButton,\n"
"TransparentToggleToolButton,\n"
"TransparentDropDownToolButton,\n"
"TransparentPushButton,\n"
"TransparentDropDownPushButton,\n"
"TransparentTogglePushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    margin: 0;\n"
"}\n"
"\n"
"TransparentToolButton:hover,\n"
"TransparentToggleToolButton:hover,\n"
"TransparentDropDownToolButton:ho"
                        "ver,\n"
"TransparentPushButton:hover,\n"
"TransparentDropDownPushButton:hover,\n"
"TransparentTogglePushButton:hover {\n"
"    background-color: rgba(0, 0, 0, 9);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:pressed,\n"
"TransparentToggleToolButton:pressed,\n"
"TransparentDropDownToolButton:pressed,\n"
"TransparentPushButton:pressed,\n"
"TransparentDropDownPushButton:pressed,\n"
"TransparentTogglePushButton:pressed {\n"
"    background-color: rgba(0, 0, 0, 6);\n"
"    border: none;\n"
"}\n"
"\n"
"TransparentToolButton:disabled,\n"
"TransparentToggleToolButton:disabled,\n"
"TransparentDropDownToolButton:disabled,\n"
"TransprentPushButton:disabled,\n"
"TransparentDropDownPushButton:disabled,\n"
"TransprentTogglePushButton:disabled {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"PillPushButton,\n"
"PillPushButton:hover,\n"
"PillPushButton:pressed,\n"
"PillPushButton:disabled,\n"
"PillPushButton:checked,\n"
"PillPushButton:checked:hover,\n"
"PillPushButton:checked:p"
                        "ressed,\n"
"PillPushButton:disabled:checked,\n"
"PillToolButton,\n"
"PillToolButton:hover,\n"
"PillToolButton:pressed,\n"
"PillToolButton:disabled,\n"
"PillToolButton:checked,\n"
"PillToolButton:checked:hover,\n"
"PillToolButton:checked:pressed,\n"
"PillToolButton:disabled:checked {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.tool_button_toggle_theme)

        self.horizontalSpacer = QSpacerItem(211, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.calendar_picker_ymd = CalendarPicker(Form)
        self.calendar_picker_ymd.setObjectName(u"calendar_picker_ymd")
        self.calendar_picker_ymd.setMinimumSize(QSize(240, 30))
        self.calendar_picker_ymd.setMaximumSize(QSize(240, 30))
        self.calendar_picker_ymd.setAutoDefault(False)


        self.verticalLayout_2.addWidget(self.calendar_picker_ymd)

        self.time_picker_hms = TimePicker(Form)
        self.time_picker_hms.setObjectName(u"time_picker_hms")
        self.time_picker_hms.setEnabled(True)
        self.time_picker_hms.setMinimumSize(QSize(240, 30))
        self.time_picker_hms.setMaximumSize(QSize(240, 30))
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

        self.verticalLayout_2.addWidget(self.time_picker_hms)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.check_box_create_time = CheckBox(Form)
        self.check_box_create_time.setObjectName(u"check_box_create_time")
        self.check_box_create_time.setMinimumSize(QSize(29, 22))
        self.check_box_create_time.setMaximumSize(QSize(90, 22))
        self.check_box_create_time.setChecked(True)

        self.verticalLayout.addWidget(self.check_box_create_time)

        self.check_box_modify_time = CheckBox(Form)
        self.check_box_modify_time.setObjectName(u"check_box_modify_time")
        self.check_box_modify_time.setMinimumSize(QSize(29, 22))
        self.check_box_modify_time.setMaximumSize(QSize(90, 22))
        self.check_box_modify_time.setChecked(True)

        self.verticalLayout.addWidget(self.check_box_modify_time)

        self.check_box_access_time = CheckBox(Form)
        self.check_box_access_time.setObjectName(u"check_box_access_time")
        self.check_box_access_time.setMinimumSize(QSize(29, 22))
        self.check_box_access_time.setMaximumSize(QSize(90, 22))
        self.check_box_access_time.setChecked(True)

        self.verticalLayout.addWidget(self.check_box_access_time)

        self.check_box_auto_clear = CheckBox(Form)
        self.check_box_auto_clear.setObjectName(u"check_box_auto_clear")
        self.check_box_auto_clear.setMinimumSize(QSize(29, 22))
        self.check_box_auto_clear.setMaximumSize(QSize(90, 22))
        self.check_box_auto_clear.setChecked(True)

        self.verticalLayout.addWidget(self.check_box_auto_clear)


        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tool_button_open_dir = ToolButton(Form)
        self.tool_button_open_dir.setObjectName(u"tool_button_open_dir")
        sizePolicy2.setHeightForWidth(self.tool_button_open_dir.sizePolicy().hasHeightForWidth())
        self.tool_button_open_dir.setSizePolicy(sizePolicy2)
        self.tool_button_open_dir.setMinimumSize(QSize(30, 30))
        self.tool_button_open_dir.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.tool_button_open_dir)

        self.push_button_change_time = PushButton(Form)
        self.push_button_change_time.setObjectName(u"push_button_change_time")
        sizePolicy.setHeightForWidth(self.push_button_change_time.sizePolicy().hasHeightForWidth())
        self.push_button_change_time.setSizePolicy(sizePolicy)
        self.push_button_change_time.setMinimumSize(QSize(205, 30))
        self.push_button_change_time.setMaximumSize(QSize(205, 30))

        self.horizontalLayout.addWidget(self.push_button_change_time)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.time_picker_hms.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.StrongBodyLabel.setText(QCoreApplication.translate("Form", u"\u8bbe\u5b9a\u5168\u5c40\u65e5\u671f", None))
#if QT_CONFIG(tooltip)
        self.time_picker_hms.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.time_picker_hms.setText("")
        self.check_box_create_time.setText(QCoreApplication.translate("Form", u"\u521b\u5efa\u65f6\u95f4", None))
        self.check_box_modify_time.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u65f6\u95f4", None))
        self.check_box_access_time.setText(QCoreApplication.translate("Form", u"\u8bbf\u95ee\u65f6\u95f4", None))
        self.check_box_auto_clear.setText(QCoreApplication.translate("Form", u"\u81ea\u52a8\u6e05\u7a7a", None))
        self.push_button_change_time.setText(QCoreApplication.translate("Form", u"\u4fee\u6539", None))
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
            file_paths = [os.path.normpath(url.toLocalFile()) for url in file_urls]
            expected_dir = [i for i in file_paths if os.path.isfile(i)]
            current_content = self.toPlainText()
            if current_content:
                expected_dir.extend(os.path.normpath(line.strip()) for line in current_content.split('\n') if
                                    line.strip() and os.path.isfile(line.strip()))
            self.signal_paste.emit(expected_dir)
        else:
            super().paste()

    def keyPressEvent(self, event):
        if event.matches(QKeySequence.Paste):
            # 执行你的操作
            self.paste()
        else:
            super().keyPressEvent(event)
