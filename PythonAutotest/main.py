import requests

HOST = 'https://api.pokemonbattle.me:9104'

create_poke = requests.post(url=f'{HOST}/pokemons',
                            json={

                                "name": "Бульбазав",
                                "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                            },
                            headers={'Content-Type': 'application/json',
                                     "trainer_token": "Введите свой токен"},
                            timeout=5)

print(create_poke.text)

change_name = requests.put(url=f'{HOST}/pokemons',
                           headers={'Content-Type': 'application/json',
                                    "trainer_token": "Введите свой токен"},
                           json={
                               "pokemon_id": "20812",
                               "name": "New Name",
                               "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                           },)

print(change_name.text)

catch = requests.post(url=f'{HOST}/trainers/add_pokeball',
                      headers={'Content-Type': 'application/json',
                               "trainer_token": "Введите свой токен"},
                      json={
                          "pokemon_id": "20812"
                      },)

print(catch.text)
