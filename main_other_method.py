# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2024/4/7 17:26
# File:main
import os
import time


def set_file_time(filename, update_time, access_time=None):
    # 传修改时间，不传访问时间
    filename = os.path.abspath(filename)
    new_update_time = time.mktime(time.strptime(update_time, '%Y-%m-%d %H:%M:%S'))

    # 如果不传访问时间，则获取文件当前的访问时间
    if access_time is None:
        new_access_time = os.path.getatime(filename)
        print(new_access_time)
    else:
        new_access_time = time.mktime(time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
    os.utime(filename, (new_access_time, new_update_time))


if __name__ == '__main__':
    set_file_time(r'D:\2\info.txt', '2032-01-08 20:50:20', access_time='2032-01-08 20:50:20')
