def list_to_dict(a):
    b = {}
    for i in a:
        b[i] = i
    return b

user_list = []
list_element = 0
while list_element != 'stop':
    list_element = input('Please input a value for list creating (input "stop" to stop creating)... ')
    if list_element != 'stop':
        user_list.append(list_element)

new_dict = list_to_dict(user_list)

print(f"New dictionary was created {new_dict}")