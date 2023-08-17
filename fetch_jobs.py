import requests


def get_jobs(position, country):
	url = "https://linkedin-jobs-search.p.rapidapi.com/"

	payload = {
		"search_terms": f"{position}",
		"location": f"{country}",
		"page": "1"
	}

	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "2e64f82d68msh8e13c521e228dfdp168c9ejsnf48b216288a9",
		"X-RapidAPI-Host": "linkedin-jobs-search.p.rapidapi.com"
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