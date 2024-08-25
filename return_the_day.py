def whatday(num):
    day = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ]
    
    if num < 1 or num > 7:
        return "Wrong, please enter a number between 1 and 7"
    else:
        return day[num - 1]