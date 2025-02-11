import time
import datetime
while True:
    tdy = datetime.date.today()
    v = datetime.date(2025,2,14)
    ttvd = 58
    for h in range(57):
        ttvd = ttvd -1
        print(ttvd)
        time.sleep(1)
        if ttvd == 0:
            break
