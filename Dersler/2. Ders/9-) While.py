import time

i = 0
while i < 20:
    i += 1
    print(i)
    if i == 12:
        break

while True:
    time.sleep(2)
    print(2)
    continue
    print(3)

