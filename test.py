import requests

BASE = "http://127.0.0.1:5000/"

data = [
        {"likes": 79, "name": "Tam", "views": 2000},
        {"likes": 12, "name": "Captain Lamb", "views": 202},
        {"likes": 10, "name": "Ella and Her Treats", "views": 2030}
      ]

for i in range(len(data)):
  response = requests.put(BASE + "video/" + str(i), data[i])
  print(response.json())


response = requests.delete(BASE + "video/0")
print(response)

input()

response = requests.get(BASE + "video/1")
print(response.json())