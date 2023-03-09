import random
from typing import Union

x: list = [x for x in range(random.randint(50, 100)) if x%2]
x[random.randint(0, len(x))] = 200

print(x)

def list_output(list: list) -> Union[str, None]:
    for i in list:
        if i != 200:
            print(i)
        else:
            return "'200' was found. Outputting has been stopped."
    return None
            
print(list_output(x))