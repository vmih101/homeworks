import calendar
from typing import Callable

month = int(input('Input the number of the month... '))

def month_to_season(month: int) -> str:
    seasons = {'winter':(12,1,2),
               'spring':(3,4,5),
               'summer':(6,7,8),
               'fall':(9,10,11)}
    for key in seasons.keys():
        if month in seasons[key]:
            return key

def title(func: Callable):
    def wrapper(func: str):
        global month
        print("*"*40)
        print("START".center(40, '-'), end= '\n\n\n')
        if func is not None:
            print(f"{calendar.month_name[month]} is the {func} month".center(40), end= '\n\n\n')
        else:
            print(f"Such month does not exist !".center(40), end= '\n\n\n')
        print("FINISH".center(40, '-'))
        print("*"*40)
    return wrapper


@title
def print_result(func: str):
    print(func)


print(print_result(month_to_season(month)))