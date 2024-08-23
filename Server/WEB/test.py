import requests

url = "http://192.168.100.10:5000/login"
json = {
	"nome":"Valquiria",
	"senha":"1234"
}

response = requests.post(url=url, json=json)
print(response.json())