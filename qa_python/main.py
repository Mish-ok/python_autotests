import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8427b4af7a37b84367876178ac92c6a0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "m-okunev@yandex.ru",
    "password": "#3op3e3opP"
}

body_confirmation = {
    "trainer_token": TOKEN,
}

body_create = {
    "name": "generate",
    "photo_id": -1
}

body_rename = {
    "pokemon_id": "42101",
    "name": "Дурпер",
    "photo_id": -1
}

body_pokeball = {
    "pokemon_id": "42101"
}

RESPONSE_POKEBALL = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_rename)
print(RESPONSE_POKEBALL.text)

'''RESPONSE_RENAME = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print(RESPONSE_RENAME.text)

RESPONSE_CREATE = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(RESPONSE_CREATE.text)

RESPONSE_REGISTRATION = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(RESPONSE.text)

RESPONSE_CONFIRMATION = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(RESPONSE_CONFIRMATION.text)'''