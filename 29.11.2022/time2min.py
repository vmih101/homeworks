import datetime

def hours_minutes(): # function returns current time like a list with two elements (hours, minutes)
    current = datetime.datetime.now()
    return current.hour, current.minute

def time2min(x): # function takes a list with two elements (hours, minutes) and returns amount of minutes
    min = x[0]*60+x[1]
    return min

def title(func):
    def wrapper(func):
        print("*"*60)
        print("START".center(60, '-'), end= '\n\n\n')
        print(f'{func} minutes have passed since the beginning of the day ⧗'.center(60), end= '\n\n\n')
        print("FINISH".center(60, '-'))
        print("*"*60)
    return wrapper

@title
def print_minutes(func):
    print(func)

print(print_minutes(time2min(hours_minutes())))


