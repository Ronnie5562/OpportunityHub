import requests


def get_jobs(position, country):
	url = "https://indeed11.p.rapidapi.com/"

	payload = {
		"search_terms": f"{position}",
		"location": f"{country}",
		"page": "1"
	}

	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "e3d24a42f3msh21f66de019442edp16dbadjsnbc611f49866a",
		"X-RapidAPI-Host": "indeed11.p.rapidapi.com"
	}

	response = requests.post(url, json=payload, headers=headers)

	return response.json()

	# print(response.json())


if __name__ == "__main__":
	position = input('What position are you looking for? ')
	country = input('Which country do you need the job in? ')

	jobs = get_jobs(position, country)
	print(jobs[0])
	print(len(jobs))