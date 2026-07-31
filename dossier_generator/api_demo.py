import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

print(response.status_code)
joke = response.json()

print("Setup:")
print(joke["setup"])

print()

print("Punchline:")
print(joke["punchline"])