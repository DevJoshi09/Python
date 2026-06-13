# Connect to an API using python
import requests
 
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    #  This is an f-string (formatted string)
    # It builds a dynamic URL
    url = f"{base_url}/pokemon/{name}" 

    # Uses the requests library
    # Sends an HTTP GET request to that URL
    # Gets data from the server

    # 👉 The result (response) contains:

    # Status code (200 = success)
    # Data (usually JSON)
    # Headers
    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        pokemon_info = response.json()
        return pokemon_info
    else:
        print("falied to retrieved data .")




pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

print(f"Name: {pokemon_info["name"].capitalize()}")
print(f"id: {pokemon_info["id"]}")
print(f"Height: {pokemon_info["height"]} lbs")
print(f"Weight: {pokemon_info["weight"]} cm")

