import json
import requests
from datetime import date

BASE_URL = "https://leetcode-stats-api.herokuapp.com/"
USERS = "bin/users.json"
COUNTS = "bin/counts.json"

with open(USERS, 'r') as f:
    global users
    data = json.load(f)
    users = data['users']

eas = 0
med = 0
har = 0

for u in users:
    stats = requests.get(BASE_URL + u).json()
    eas += stats['easySolved']
    med += stats['mediumSolved']
    har += stats['hardSolved']

today = date.today()
today = today.strftime('%d-%m-%Y')

easEntry = {
    "date": today,
    "count": eas,
    "difficulty": "easy"
}

medEntry = {
    "date": today,
    "count": med,
    "difficulty": "medium"
}

harEntry = {
    "date": today,
    "count": har,
    "difficulty": "hard"
}

output = {}
with open(COUNTS, 'r') as f:
    data = json.load(f)
    logs = data['logs']
    logs.append(easEntry)
    logs.append(medEntry)
    logs.append(harEntry)
    output = {"logs": logs}

with open(COUNTS, 'w') as f:
    json.dump(output, f)

