a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in b: # is looking for the same elements and adds them to the list
    if i in a:
        c.append(i)

print(c)
