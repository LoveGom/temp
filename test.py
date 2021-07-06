import time
from datetime import datetime


while(True):
    try:
        date = datetime.now()
        print(date.hour, date.minute, date.second)
        if date.hour == 16 and date.minute == 52:
            print("True")
        else:
            print("False")
        time.sleep(1)
    except KeyboardInterrupt:
        print("종료됨")
        exit()
