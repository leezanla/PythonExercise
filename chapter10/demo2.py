#encoding=gbk
import schedule
import time


def fun():
    print("hello world")


schedule.every(3).seconds.do(fun)
while True:
    schedule.run_pending()
    time.sleep(1)






























