import requests
import json



headers = {
        'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
        'x-rapidapi-key': "1ba896e9a4mshe53ad1d4f1869c8p10ab9djsna6c21e629564"
        }

def random_recipe():

    
    url = "https://the-cocktail-db.p.rapidapi.com/random.php"
    
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)


    return data


def filter_by_ingredients(list_of_ingredients):

    query = ""
    for ingredient in list_of_ingredients:

        query += ","+ingredient
    query = query[1:]


    url = "https://the-cocktail-db.p.rapidapi.com/filter.php"

    querystring = {"i":query}

   
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    
    return data




def full_cocktail_details(drink_id):

    url = "https://the-cocktail-db.p.rapidapi.com/lookup.php"

    querystring = {"i":str(drink_id)}

    
    response = requests.request("GET", url, headers=headers, params=querystring)


    # with open("test2.json", "w") as file:
    #     file.write(str(response.text))

    data = json.loads(response.text)


    print(data)

    
    return data


# data = full_cocktail_details(11007)

# drinks = data.get("drinks")[0]
data = filter_by_ingredients(['rum', 'lemon juice'])

print(data)