import requests

class Futurama:
    def __init__(self):
        self.url = "https://futurama-dam.web.app/api/v1/"
    
    def characters(self):
        url = self.url + 'characters?limit=427'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['hits']]

            
    def charactersDead(self):
        url = self.url + 'characters?limit=427'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['hits'] if character['status'] == 'DEAD']
    
    def charactersByGender(self, gender):
        url = self.url + 'characters?limit=427'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['hits'] if character['gender'] == gender.upper()]
        
    def humans(self):
        url = self.url + 'characters?limit=427'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return [character['name'] for character in data['hits'] if character['species'] == 'HUMAN']
    
    def episode(self, season, episode):
        url = self.url + 'seasons'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            for season_id in data:
                if season_id['id'] == season:
                    for episode_id in season_id['episodes']:
                        if episode_id['id'] == episode:
                            return episode_id['name']
            return "Episode not found"
    
    def species(self):
        url = self.url + 'characters?limit=427'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            return list(set([species['species'] for species in data['hits']]))
        

futurama = Futurama()
print(futurama.characters())
print(futurama.charactersDead())
print(futurama.charactersByGender('unknown'))
print(futurama.humans())
print(futurama.episode(1, 1))
print(futurama.species())