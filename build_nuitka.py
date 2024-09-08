# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/14 22:24
# File:build_nuitka
cmd = """

nuitka --windows-icon-from-ico="logo.ico" app.py --disable-console --standalone --file-version=1.0 --onefile --enable-plugin=pyside2 --include-data-files="D:\files\Documents\study\python\Program\file_date_changer\res\logo.ico=@logo.ico" --copyright="Copyright (C) 2024 Gentlesprite."
nuitka --standalone --enable-plugin=pyside2 --show-memory --show-progress --onefile --disable-console --output-dir=output --file-version=1.0 --windows-icon-from-ico="res/logo.ico" --output-filename="FileDateChanger.exe" --copyright="Copyright (C) 2024 Gentlesprite." app.py
"""

"""
版本号分级（软件版本号及自己的项目首次版本号选择）
平时大家肯定会碰到不同的软件版本号，那么这些版本号是依照什么标准设立和升级变化的呢？
如果我们自己做开源项目，版本号又该怎么设定呢？
简单的概括如下。
版本号一般为 A.B.C ，如 4.5.6 版本

A—第一级：重大重构
B—第二级：重大功能改进
C—第三极：小升级或者BUG修复
我们也会看到有0.0.5或者0.5.0这样的版本号，也有1.0.0此类版本号。那我们做开源项目的第一个版本号为什么比较好呢?
其实可以理解为

0.x.x 是非正式版本
1.x.x 是正式发布版本
"""

import os
from app import APP

app_name = APP.software_name
ico_path = '../../res/logo0.4.ico'
output = 'output'
main = 'app.py'
enable_plug = 'pyside6'
file_version = APP.software_name_version
author = APP.software_name_author
copy_right = f'Copyright (C) 2024 {author}.'
include_module = r'ui_sec_menu,res_rc,ui'
build_command = f'nuitka --standalone --enable-plugin={enable_plug} --show-memory --show-progress --onefile '
build_command += f'--disable-console --output-dir={output} --file-version={file_version} '
build_command += f'--windows-icon-from-ico="{ico_path}" '
build_command += f'--output-filename="{app_name}.exe" --copyright="{copy_right}" --include-package=qfluentwidgets --include-module=qfluentwidgets --include-module={include_module} --mingw64 '
build_command += main
print(build_command)
# todo 获取当前版本并确认后才开始打包,以免系统环境变量非当前程序环境
os.system(build_command)
