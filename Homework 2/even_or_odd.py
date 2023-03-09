def isInt(value): # function for checking if value is an integer
    try:
        int(value)
        return True
    except ValueError:
        return False

num = input('Input an integer ...')

while isInt(num) is not True: # force user to enter an valid integer
    print(f"{num} is not an integer.")
    num = input('Please input a valid integer ...')

num = int(num)

if num%2 == 0: # check for parity
    print(f"{num} is an even integer.")
else:
    print(f"{num} is an odd integer.")
