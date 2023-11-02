import requests

url = "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/cncidr.txt"
response = requests.get(url)
response.raise_for_status()  # This will check for errors

with open('data.txt', 'wb') as file:
    file.write(response.content)
