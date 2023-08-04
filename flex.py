import requests

def search_indeed_jobs(query, location, api_key):
    base_url = 'https://api.indeed.com/ads/apisearch'
    params = {
        'q': query,
        'l': location,
        'format': 'json',
        'publisher': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for errors in the response
        job_data = response.json()
        
        # Process the job data here, extract relevant information, and display results
        for job in job_data['results']:
            print(f"Job Title: {job['jobtitle']}")
            print(f"Company: {job['company']}")
            print(f"Location: {job['formattedLocation']}")
            print(f"URL: {job['url']}")
            print('---')
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

indeed_api_key = ''
search_query = 'Python Developer'
search_location = 'New York, NY'

search_indeed_jobs(search_query, search_location, indeed_api_key)
