import os
import sys
from datetime import datetime
from typing import Optional
from PySide6.QtCore import Qt, QLocale, QTranslator, Signal, QDateTime
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFileDialog, QTableWidgetItem, QMainWindow, QDialog, \
    QHeaderView
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QCalendarWidget, QPushButton, QAbstractButton, QWidget, QMenu
from loguru import logger
from qfluentwidgets import FlyoutViewBase, BodyLabel, PrimaryPushButton, RoundMenu, TableItemDelegate
from qfluentwidgets.components.dialog_box import MessageBox
from qfluentwidgets.common import FluentIcon as FIF
from win32file import CreateFile, SetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
import res_rc
import win32timezone

from qfluentwidgets import CheckBox
from qfluentwidgets import PushButton
from qfluentwidgets import CalendarPicker
from qfluentwidgets import TimePicker
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import TextEdit
from qfluentwidgets import TableWidget

from qfluentwidgets.components.date_time import calendar_picker, time_picker, date_picker
from qfluentwidgets.components.widgets import *
from qfluentwidgets import *
from ui import Ui_MainWindow
from ui_sec_menu import Ui_Dialog

from enum import Enum
from qfluentwidgets import StyleSheetBase, Theme, isDarkTheme, qconfig