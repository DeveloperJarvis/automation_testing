import requests
import json

# Set the base URL for the API
base_url = "https://dev.api.edu-collab.com/courses/edit/course_details"

# Set the headers for the request
headers = {
  "Authorization": "Bearer YOUR_ACCESS_TOKEN",
  "Content-Type": "application/json",
}

# Set the payload for the request
payload = {
  "name": "My New Course",
  "description": "This is a new course that I am creating.",
}

# Make the request to the API
response = requests.patch(base_url, headers=headers, data=json.dumps(payload))

# Check the status code of the response
if response.status_code == 200:
  # The request was successful
  print("The course was updated successfully.")
else:
  # The request failed
  print("The request failed with status code {}.".format(response.status_code))