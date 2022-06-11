import datetime


def current_time():
    current_time=datetime.datetime.now()

    print(current_time.strftime("%A"))
    print(current_time.strftime("%I:%M %p"))
    print(current_time.strftime("%d-%b-%Y"))