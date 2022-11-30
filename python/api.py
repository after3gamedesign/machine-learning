import requests
import json

r = requests.get("https://api.glitch.com/")
j=r.json()
print(j)

