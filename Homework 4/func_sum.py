def sum(start, end): # this function returns sum of the range of values from start to end (Start and End are integers)
    sum = 0
    if end < start: # we should swap values if first value is greater than second
        start, end = end, start
    for i in range(start, end+1): 
        sum = sum + i
    return sum

start, end = int(input('Input firts value fo the range ...')), int(input('Input second value fo the range ...'))

print(f"Sum of all values in range is {sum(start, end)}.") # adjust the range of integers