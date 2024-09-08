# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/14 22:09
# File:build
import os
import PyInstaller.__main__

py_name = "app.py"
icon_path = r"/res/logo.ico"
upx_dir = r"D:\env\upx\upx-4.2.3-win64"
version_file = os.path.join(os.getcwd(), 'file_version_info.txt')

PyInstaller.__main__.run([
    '--upx-dir', upx_dir,
    '-F',
    '-w',
    '-i', icon_path,
    '--version-file', version_file,
    '--hidden-import=pywintypes',
    py_name
])
