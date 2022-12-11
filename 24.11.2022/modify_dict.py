import random, string

c = string.ascii_lowercase + string.digits # set of characters for string
dict = {}

for i in range(random.randint(5, 10)): # random number generator from a to b for generating random length of dictionary
    dict[i+1] = ''.join(random.sample(c,10)) # creates a random string without tabs (it's possible to use any character as a separator instead of '') 
    # random.sample creates a list of string and we should use .join
    # 

x = dict.popitem() # it deletes last element from the dictionary and return it to the variable (work in python 3.7 and later!)

dict[x[0]] = dict[1] # it takes key from x and value (key = 1) from dict
dict[1] = x[1] # it takes value from x and rewrite it for key '1' in the dictionary
del dict[2] # deletes key '2' from the dictionary
dict['new_key'] = 'new_value' # it creates new element in the dictionary

print(dict.items()) 