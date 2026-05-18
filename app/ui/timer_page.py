"""

A timer:
    1- User will say how much time does he/she need (usually in hours)
        - By defult is 2 hours
    2- User will define the brak time (like A break for each 20 min)
        - By defult it will be each 20 minutes
"""
from datetime import datetime, timedelta, time

def study_time(time_duration: float = 2) -> None:
    """This function set a duration for study or work. By defult the time is 2 hours.

    Args:
        time_duration (float): set a duration. Defaults to 2.
    """
    duration: timedelta = timedelta(hours=time_duration)
    print(f"Total seconds: {duration.total_seconds()}") # for purpose debug 

study_time()