# ADD YOUR IMPORTS HERE


# PLEASE DO NOT MAKE CHANGES BELOW THIS LINE

def get_simpsons_quote():
    r = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")

    body = json.loads(r.content)[0]

    return f"{body['character']}: {body['quote']}"


print(get_simpsons_quote())
