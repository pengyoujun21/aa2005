

fw = open("new.png","wb")



fr = open("top.png","rb")
while True:
    data = fr.read(1024)
    print("---r----")
    if not data:
        fr.close()
        break
    fw.write(data)
print("---1----")
fr = open("bot.png", "rb")
while True:

    data = fr.read(1024)
    if not data:
        fr.close()
        break
    fw.write(data)
print("---2----")

fw.close()