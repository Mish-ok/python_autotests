import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8427b4af7a37b84367876178ac92c6a0'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '4435'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Попандос'

@pytest.mark.parametrize('key, value', [('name', 'Дурпер'), ('trainer_id', TRAINER_ID), ('id', '42101')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
