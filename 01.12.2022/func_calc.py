from typing import Callable

a: float = float(input('Input first number ... '))
operator: str = input('Input operator ... ')
while operator not in ('+', '-', '*', '/'):
    operator = input('\033[31mOperation is not supported ! \033[0m Input correct operator as + , - , * , / ... ') # print error message if user inputs invalid operator
b: float = float(input('Input second number ... '))

def calc(a:float, b: float, operator: str) -> float: # converts arguments to string and calculates the result with operator eval
    answer: float = float(eval(str(a)+operator+str(b)))
    return answer

def title(func: Callable):
    def wrapper(func: float):
        global a, b, operator
        print("*"*40)
        print("START".center(40, '-'), end= '\n\n\n')
        print(f"{a:g} {operator} {b:g} = {func:g}".center(40), end= '\n\n\n') # {float:g} truncate floats if decimal part is null (just for beauty)
        print("FINISH".center(40, '-'))
        print("*"*40)
    return wrapper


@title
def print_result(func: float):
    print(func)

print(print_result(calc(a, b, operator)))



