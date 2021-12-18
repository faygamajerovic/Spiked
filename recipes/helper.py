def ingredients_processor(dictionary_of_drink):
    ingredients_list = []
    for key in dictionary_of_drink:

        if 'Ingredient' in key:
            if dictionary_of_drink[key] == None:
                continue
            else:
                ingredients_list.append(dictionary_of_drink[key])

    return ingredients_list