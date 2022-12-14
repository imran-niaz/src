import requests

# Prompt the user for a URL
url = input("Enter a URL: ")

# Send a request to the URL and save the response
response = requests.get(url)

# Write the response to a file in the specified folder
with open("./responses/response.txt", "w") as file:
    file.write(response.text)
