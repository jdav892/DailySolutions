from datetime import datetime

def period_is_late(last, today, cycle_length):
    days = (today - last).days
    return days > cycle_length