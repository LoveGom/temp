import time
from datetime import datetime


while(True):
    try:
        date = datetime.now()
        print(date.hour, date.minute, date.second)
        time.sleep(1)
    except KeyboardInterrupt:
        print("종료됨")
        exit()
