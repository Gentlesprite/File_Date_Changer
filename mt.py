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
        createTimes = Time(time.localtime(createTime + offset[0]))
        accessTimes = Time(time.localtime(accessTime + offset[1]))
        modifyTimes = Time(time.localtime(modifyTime + offset[2]))
        SetFileTime(fh, createTimes, accessTimes, modifyTimes)
        CloseHandle(fh)
        return 0
    except Exception as e:
        return e