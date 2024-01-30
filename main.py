import requests
from datetime import datetime, timedelta

Api_key = "37f79cecf91d468eba866f8758a69dcd"
url = "https://api.football-data.org/v2/competitions/PL/matches?season=2023"



headers = {
    "X-Auth-Token": Api_key
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    fixtures = response.json()["matches"]
    print(' ---------------------------------')
    print('| Premier League 2023-2024 Season |')
    print(' ---------------------------------')
    print()
    for fixture in fixtures:
        # Convert the UTC date and time to Mauritian time (GMT+4)
        utc_datetime = datetime.fromisoformat(fixture["utcDate"])
        mauritian_datetime = utc_datetime + timedelta(hours=4)

        # Split the date and time and add a space between them
        date_time = mauritian_datetime.strftime("%Y-%m-%d %H:%M:%S").split(" ")
        print(fixture["homeTeam"]["name"], "vs", fixture["awayTeam"]["name"], "on", date_time[0], 'at', date_time[1], 'O\'Clock Mauritian Time')
        print('----------------------------------------------------------------------------------------------------------')
else:
    print("Error:", response.status_code)