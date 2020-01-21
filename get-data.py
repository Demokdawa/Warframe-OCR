import json
import requests

url = 'https://drops.warframestat.us/data/relics.json'

resp = requests.get(url=url)
data = resp.json()

# print(data['relics'][2]) #Full data for the third relics

# print(data['relics'][2]['rewards'])

r_era = data['relics'][2]['tier']
r_name = data['relics'][2]['relicName']
r_quality = data['relics'][2]['state']

r_reward_1 = data['relics'][2]['rewards'][0]['itemName']
r_reward_2 = data['relics'][2]['rewards'][1]['itemName']
r_reward_3 = data['relics'][2]['rewards'][2]['itemName']
r_reward_4 = data['relics'][2]['rewards'][3]['itemName']
r_reward_5 = data['relics'][2]['rewards'][4]['itemName']
r_reward_6 = data['relics'][2]['rewards'][5]['itemName']


print('')

