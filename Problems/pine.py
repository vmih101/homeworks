x = int(input(f'Введите ширину основания ёлочки... '))
a = 1
b = x//2
print('Start ...', end= '\n\n')
while a < x:
    if a == 1:
        print(' '*b + '☆'*a)
        a += 2
        b -= 1
    else:    
        print(' '*b + '✲'*a)
        a += 2
        b -= 1
if a == x+1:
    print(f'\nFinish!')