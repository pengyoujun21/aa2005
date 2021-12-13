"""
    读取一个文件，把文件平均分成两部分，分别存入两个文件，然后通过两个进程进行操作
"""

import os
from multiprocessing import Process





def top(file_name):
    filesize = os.path.getsize(file_name)
    fr = open(file_name,"rb")
    fw = open("top.png","wb")
    pos = filesize // 2
    while pos > 1024:
        fw.write(fr.read(1024))
        pos -= 1024
    else:
        fw.write(fr.read(pos))

def bottom(file_name):
    filesize = os.path.getsize(file_name)
    fr = open(file_name, "rb")
    fw = open("bot.png", "wb")
    pos = filesize // 2
    fr.seek(pos,0)
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)

if __name__ == '__main__':
    file_name = "20211126225427.png"
    p = Process(target=top,kwargs={"file_name":file_name})
    p.start()

    # p1 = Process(target=bottom, kwargs={"file_name":file_name})
    # p1.start()

    p.join()
    p1.join()