import requests

url = "https://code.jquery.com/jquery-3.3.1.min.js"
response = requests.get(url)

with open("jquery-3.3.1.min.js", "wb") as f:
    f.write(response.content)
