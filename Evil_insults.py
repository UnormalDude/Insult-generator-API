import requests
import json
import pyperclip

response = requests.get(f"https://evilinsult.com/generate_insult.php?lang=en&type=json")

#print(response.json()['insult'])
pyperclip.copy(response.json()['insult'])
#input()
