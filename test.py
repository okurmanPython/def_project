import requests

city = "Bishkek"
api_key = "bc8ea82069ab120f1c2c671cc8a0dd10"
data = requests.get("https://dog.ceo/api/breeds/image/random").json()
# data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric').json()
print(data)