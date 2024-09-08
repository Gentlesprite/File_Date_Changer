# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/14 19:54
# File:main
from win32file import CreateFile, SetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
import pywintypes
from pywintypes import Time
import time

def modifyFileTime(filePath, createTime, modifyTime, accessTime, offset=(0, 1, 2)):
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
        createTimes = Time(createTime + offset[0])
        accessTimes = Time(accessTime + offset[1])
        modifyTimes = Time(modifyTime + offset[2])
        SetFileTime(fh, createTimes, accessTimes, modifyTimes)
        CloseHandle(fh)
        return 0
    except Exception as e:
        return e

# if __name__ == '__main__':
#     # 需要自己配置
#     cTime = 1576258262  # 创建时间（时间戳）
#     mTime = 1549060863  # 修改时间（时间戳）
#     aTime = 1549060864  # 访问时间（时间戳）
#     fName = r"D:\2\info.txt"  # 文件路径，文件存在才能成功（可以写绝对路径，也可以写相对路径）
#
#
#
#     # 调用函数修改文件创建时间，并判断是否修改成功
#     r = modifyFileTime(fName, cTime, mTime, aTime, offset)
#     if r == 0:
#         print('修改完成')
#     elif r == 1:
#         print('修改失败')
