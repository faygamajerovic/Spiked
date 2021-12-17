def random_recipe():

    import requests
    import json
    url = "https://the-cocktail-db.p.rapidapi.com/random.php"
    headers = {
        'x-rapidapi-host': "the-cocktail-db.p.rapidapi.com",
        'x-rapidapi-key': "1ba896e9a4mshe53ad1d4f1869c8p10ab9djsna6c21e629564"
        }
    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    return data