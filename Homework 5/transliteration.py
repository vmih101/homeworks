latin: str = 'helowrd' 
cyrillic: str = 'хеловрд'
abc: dict = dict(zip(latin, cyrillic)) # zip is used to combine iterated objects. dict() transforms zip objects to dictionary

text: str = 'hello world!'

def translit(text: str, abc: dict) -> str:
    new_text: str = '' # we have to create a new string here because string is immutable object. Remember it!!!
    for i in text:
        if i in abc.keys(): # check that i is in the dictionary
            new_text = new_text + abc.get(i) # add value to string
        else:
            new_text += i
    return new_text

print(translit(text, abc))