import requests
import time
while True:
    response = requests.get("https://v2rayn.daniel20120223.repl.co")
    print(response.text)
    time.sleep(30)
