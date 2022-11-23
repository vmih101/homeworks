import math
x = 0
a = math.isfinite(x)
print(a)

nums = [0] * 3 # Empty list
counter = 1
for x in range(len(nums)): #len returns the size of the list "nums"
    print(f"Please input an integer {counter}...")
    counter += 1
    nums[x] = int(input()) # inserts the value into the list
nums.sort(reverse=True) # sorts the list ('reverse=True' sorts in descending order)
print(f"The largest number is {nums[0]}")