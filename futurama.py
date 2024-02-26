import requests

def characters():
    url = 'https://futurama-dam.web.app/api/v1/characters?limit=427'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        characters = [character['name'] for character in data['hits']]
        print(characters)
        
def charactersDead():
    url = 'https://futurama-dam.web.app/api/v1/characters?limit=427'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        characters = [character['name'] for character in data['hits'] if character['status'] == 'DEAD']
        print(characters)
        
def charactersByGender(gender):
    url = 'https://futurama-dam.web.app/api/v1/characters?limit=427'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        characters = [character['name'] for character in data['hits'] if character['gender'] == gender.upper()]
        print(characters)
    
characters()
charactersDead()
charactersByGender("male")