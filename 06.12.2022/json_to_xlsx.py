import requests
import pandas as pd


def json_cocktails_to_table():
    response = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = response.json()
    new_data = {} # empty dict as future dataframe object
    names, instr, img = [], [], [] # amount of columns
    for i in data['drinks']: # add values to lists
        names.append(i['strDrink'])
        instr.append(i['strInstructions'])
        img.append(i['strDrinkThumb'])
    new_data['Cocktail'] = names
    new_data['Instruction'] = instr
    new_data['Link to photo'] = img
    df = pd.DataFrame(new_data)   
    df.to_excel('json_output/cocktails.xlsx', index=False)

json_cocktails_to_table()