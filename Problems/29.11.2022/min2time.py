import datetime

def minutes(): # function returns the number of minutes for current day
    minutes = datetime.datetime.now().minute + datetime.datetime.now().hour * 60
    return minutes

def min2time(minutes):
    time = datetime.time(hour= minutes//60, minute= minutes%60)
    return time

def title(func):
    def wrapper(func):
        print("*"*40)
        print("START".center(40, '-'), end= '\n\n\n')
        print(f"It's {func.strftime('%H:%M')} now!".center(40), end= '\n\n\n')
        print("FINISH".center(40, '-'))
        print("*"*40)
    return wrapper

@title
def print_time(func):
    print(func)

print(print_time(min2time(minutes())))