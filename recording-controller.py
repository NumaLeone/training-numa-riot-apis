import requests
import json

url = "https://127.0.0.1:2999/replay/recording"

payload = json.dumps({
    "codec": "webm",
    "endTime": 15,
    "framesPerSecond": 5,
    "path": "C:/Users/numal/Lab3/recordings/replay6.webm",
    "startTime": 0,
    "recording": True
})
headers = {
    'api_key': 'api-key',
    'Content-Type': 'application/json'
}

response = requests.request(
    "POST", url, headers=headers, data=payload, verify=False)

print(response.text)
