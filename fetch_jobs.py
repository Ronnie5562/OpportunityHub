import requests

url = "https://indeed11.p.rapidapi.com/"

payload = {
	"search_terms": "sales manager",
	"location": "United States",
	"page": "1"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "3ab6966de4msh9fc4c26290ed4b9p17e81djsn6ebf940f7303",
	"X-RapidAPI-Host": "indeed11.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())