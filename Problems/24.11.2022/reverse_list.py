from random import randint

N = 10
a = []
b = []

for i in range(N):
    a.append(randint(1, 99))
    b.append(randint(1, 99))

print(str(a))
print(str(b))

for i in range(N-1): # approach 1
    for j in range(N-i-1):
        a[j], a[j+1] = a[j+1], a[j]

b.reverse() # approach 2

print(str(a))
print(str(b))

