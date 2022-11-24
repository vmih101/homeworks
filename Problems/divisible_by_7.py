nums = list(range(66,9999))
divisible = []
for x in nums:
    if x%7 == 0:
        divisible.append(x)
print(f"{len(divisible)} divisible numbers are in range")