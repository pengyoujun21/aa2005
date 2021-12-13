"""
线程互斥
"""
from threading import Thread,Event

msg = None  #线程通信
e = Event()
def 杨子荣():
    print("扬子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set()

t = Thread(target=杨子荣)
t.start()

print("说对口令才是自己人")
e.wait()
if msg =="天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你说对的人")
else:
    print("打死他.....无情啊.....")