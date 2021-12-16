def random_recipe():


    
    import requests

    import json


    url = "https://the-cocktail-db.p.rapidapi.com/random.php"

    headers = {
        'x-rapidapi-host': "replace host",
        'x-rapidapi-key': "replace key"
        }

    response = requests.request("GET", url, headers=headers)

    data = json.loads(response.text)

    return data