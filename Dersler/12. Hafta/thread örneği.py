import threading


def F1():
    for i in range(1, 100000):
        print(i, "*"*10)


def F2():
    for i in range(1, 100000):
        print("a", "."*10)

thread = threading.Thread(target=F1)
thread2 = threading.Thread(target=F2)

thread.start()
thread2.start()