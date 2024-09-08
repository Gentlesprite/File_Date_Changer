# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/14 22:24
# File:build_nuitka
cmd = """

nuitka --windows-icon-from-ico="logo.ico" app.py --disable-console --standalone --file-version=1.0 --onefile --enable-plugin=pyside2 --include-data-files="D:\files\Documents\study\python\Program\file_date_changer\res\logo.ico=@logo.ico" --copyright="Copyright (C) 2024 Gentlesprite."
nuitka --standalone --enable-plugin=pyside2 --show-memory --show-progress --onefile --disable-console --output-dir=output --file-version=1.0 --windows-icon-from-ico="res/logo.ico" --output-filename="FileDateChanger.exe" --copyright="Copyright (C) 2024 Gentlesprite." app.py
"""

import os

app_name = 'FileDateChanger'
ico_path = '../../res/logo.ico'
output = 'output'
main = 'app.py'
enable_plug = 'pyside6'
file_version = '0.4'
copy_right = 'Copyright (C) 2024 Gentlesprite.'
include_module = r'ui_sec_menu,res_rc,ui'
build_command = f'nuitka --standalone --enable-plugin={enable_plug} --show-memory --show-progress --onefile '
build_command += f'--disable-console --output-dir={output} --file-version={file_version} '
build_command += f'--windows-icon-from-ico="{ico_path}" '
build_command += f'--output-filename="{app_name}.exe" --copyright="{copy_right}" --include-package=qfluentwidgets --include-module=qfluentwidgets --include-module={include_module} '
build_command += main
print(build_command)
# todo 获取当前版本并确认后才开始打包,以免系统环境变量非当前程序环境
os.system(build_command)
