import requests
from datetime import datetime, timedelta

url = "https://api.football-data.org/v2/competitions/PL/matches?season=2023"

headers = {
    "X-Auth-Token": "API"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    fixtures = response.json()["matches"]
    man_united_fixtures = []

    for fixture in fixtures:
        # Check if the fixture involves Manchester United
        if fixture["homeTeam"]["name"] == "Manchester United FC" or fixture["awayTeam"]["name"] == "Manchester United FC":
            # Convert the UTC date and time to Mauritian time (GMT+4)
            utc_datetime = datetime.fromisoformat(fixture["utcDate"])
            mauritian_datetime = utc_datetime + timedelta(hours=4)

            # Split the date and time and add a space between them
            date_time = mauritian_datetime.strftime("%Y-%m-%d %H:%M:%S").split(" ")
            man_united_fixtures.append((fixture["homeTeam"]["name"], fixture["awayTeam"]["name"], date_time[0], date_time[1]))

    if len(man_united_fixtures) > 0:
        print()
        for fixture in man_united_fixtures:
            print(fixture[0], "vs", fixture[1], "on", fixture[2], "at", fixture[3], "O\'Clock Mauritian Time")
            print("-----------------------------------------------------------------------------------------------------")
    else:
        print("No fixtures involving Manchester United found.")
else:
    print("Error:", response.status_code)
