# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/14 22:24
# File:build_nuitka
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
os.system(build_command)
