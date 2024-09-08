# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sec_menuBJkiAA.ui'
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
from qfluentwidgets import TableWidget


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(360, 224)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(360, 224))
        Dialog.setMaximumSize(QSize(360, 224))
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_widget_sec_info_bar = TableWidget(Dialog)
        self.table_widget_sec_info_bar.setObjectName(u"table_widget_sec_info_bar")

        self.verticalLayout_2.addWidget(self.table_widget_sec_info_bar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.calendar_picker_ymd = CalendarPicker(Dialog)
        self.calendar_picker_ymd.setObjectName(u"calendar_picker_ymd")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.calendar_picker_ymd.sizePolicy().hasHeightForWidth())
        self.calendar_picker_ymd.setSizePolicy(sizePolicy1)
        self.calendar_picker_ymd.setMinimumSize(QSize(240, 33))
        self.calendar_picker_ymd.setMaximumSize(QSize(240, 33))

        self.verticalLayout.addWidget(self.calendar_picker_ymd)

        self.time_picker_hms = TimePicker(Dialog)
        self.time_picker_hms.setObjectName(u"time_picker_hms")
        sizePolicy1.setHeightForWidth(self.time_picker_hms.sizePolicy().hasHeightForWidth())
        self.time_picker_hms.setSizePolicy(sizePolicy1)
        self.time_picker_hms.setMinimumSize(QSize(240, 30))
        self.time_picker_hms.setMaximumSize(QSize(240, 30))
        self.time_picker_hms.setSecondVisible(True)

        self.verticalLayout.addWidget(self.time_picker_hms)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.push_button_ok = PushButton(Dialog)
        self.push_button_ok.setObjectName(u"push_button_ok")
        sizePolicy1.setHeightForWidth(self.push_button_ok.sizePolicy().hasHeightForWidth())
        self.push_button_ok.setSizePolicy(sizePolicy1)
        self.push_button_ok.setMinimumSize(QSize(90, 70))
        self.push_button_ok.setMaximumSize(QSize(90, 70))

        self.horizontalLayout.addWidget(self.push_button_ok)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.push_button_ok.setText(QCoreApplication.translate("Dialog", u"\u786e\u5b9a", None))
    # retranslateUi
