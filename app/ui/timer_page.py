"""

A timer:
    1- User will say how much time does he/she need (usually in hours)
        - By defult is 2 hours
    2- User will define the brak time (like A break for each 20 min)
        - By defult it will be each 20 minutes
"""
from datetime import datetime, timedelta
from time import sleep


def study_time(total_duration: int = 2, study_time: int = 20, break_time: int = 5):
    # total_duration -> total hours for study like 2 hours
    # study_time is focus time before a break like 20 minutes
    # break_time is like 5 minutes time until next study_time began

    duration: timedelta = timedelta(hours=total_duration) # 2:00:00
    total_second = duration.total_seconds() # 7200.0 

    for i in range(int(total_second)):
        duration -= timedelta(seconds=1)
        print(duration)
        sleep(1)
        
    # TODO 1- each 20 minutes the timer should give break for 5 minutes

    print("Nice work man!")
study_time()