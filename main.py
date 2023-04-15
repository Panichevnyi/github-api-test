import requests

# Set up authentication with personal access token
headers = {
    'Authorization': 'token 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'
}

# Define the endpoint URL for creating a new issue
url = 'https://api.github.com/repos/Panichevnyi/github-api-test/issues'

# Define the JSON payload for the new issue
payload = {
    'title': 'New task',
    'body': 'This is a new task that needs to be completed.',
    'labels': ['task']
}

# Send a POST request to create the new issue
response = requests.post(url, headers=headers, json=payload)

# Check the response status code to ensure the issue was created successfully
if response.status_code == 201:
    print('New task created successfully!')
else:
    print('Error creating new task:', response.text)
