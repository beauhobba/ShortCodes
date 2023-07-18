# pylint: disable-all


from apscheduler.schedulers.blocking import BlockingScheduler

import requests
API_WEBSITE = "https://api.open-meteo.com/v1/forecast?\
latitude=52.52&longitude=13.41&current_weather=true"

sched = BlockingScheduler()

def main():
    response = requests.get(API_WEBSITE)
    response_json = response.json()
    print(f"{response_json['current_weather']['temperature']}°C")

sched.add_job(main, 'interval', days=2)
sched.start()