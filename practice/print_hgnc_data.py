import pprint
import json
import requests

# URL of the JSON data
url = "https://g-a8b222.dd271.03c0.data.globus.org/pub/databases/genenames/hgnc/json/hgnc_complete_set.json"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Pretty print the JSON data
    print(json.dumps(data, indent=4))
else:
    print("Failed to fetch data:", response.status_code)

