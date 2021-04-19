import requests
import json

# URL for the web service, should be similar to:
scoring_uri = 'http://02c760bb-9f7b-4c00-85fb-a94ad0030cc3.southcentralus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'DGElI2iWjrG5ucSqnJUcwqBvZxq4BoTW'

# Two sets of data to score, so we get two results back
data = {"data":
        [
          {
            "mean_radius":12.45,
            "mean_texture":15.7, 
            "mean_perimeter":82.57,
            "mean_area":477.1,
            "mean_smoothness":0.1278
            },
          {
            "mean_radius":15.1,
            "mean_texture":16.39,
            "mean_perimeter":99.58,
            "mean_area":674.5,
            "mean_smoothness":0.115
          },
      ]
    }
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
