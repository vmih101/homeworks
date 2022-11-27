import random, string

c = string.ascii_lowercase + string.digits # set of characters for string
random_list = []

for i in range(random.randint(5, 20)): # random number generator from a to b for generating random length of list
    random_list.append(''.join(random.sample(c, 10))) # creates a random string without tabs (it's possible to use any character as a separator instead of '') 
    random_list.append('') # inserts empty string into the list

while random_list.count('') > 0:
    random_list.remove('') # removes empty string from the list
