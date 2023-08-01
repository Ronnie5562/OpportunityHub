import requests

url = "https://indeed-indeed.p.rapidapi.com/apisearch"

querystring = {"publisher":"<REQUIRED>","v":"2","format":"json","callback":"<REQUIRED>","q":"java","l":"austin, tx","sort":"<REQUIRED>","radius":"25","st":"<REQUIRED>","jt":"<REQUIRED>","start":"<REQUIRED>","limit":"<REQUIRED>","fromage":"<REQUIRED>","highlight":"<REQUIRED>","filter":"<REQUIRED>","latlong":"<REQUIRED>","co":"<REQUIRED>","chnl":"<REQUIRED>","userip":"<REQUIRED>","useragent":"<REQUIRED>"}

headers = {
	"X-RapidAPI-Key": "3ab6966de4msh9fc4c26290ed4b9p17e81djsn6ebf940f7303",
	"X-RapidAPI-Host": "indeed-indeed.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())