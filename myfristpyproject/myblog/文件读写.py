import os
import os.path


def file_write():
    fileHandle = open('test.txt', 'wb')
    fileHandle.writelines('\nthis is a jack')
    fileHandle.close()


file_write()


def file_read():
    fileHandle = open('test.txt')
    print(fileHandle.readline())
    fileHandle.seek(1)
    fileHandle.close()


file_read()
