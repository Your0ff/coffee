import requests
import json
url = "https://coffee.alexflipnote.dev/random.json"
r = requests.get(url)
print(r.json()['file'])
