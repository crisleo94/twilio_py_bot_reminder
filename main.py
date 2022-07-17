import os
from flask import Flask
from dotenv import load_dotenv
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()

sched = BlockingScheduler()


def job_function():
    send_message()


sched.add_job(job_function, 'cron', month='*', day_of_week='sun', hour='20')
sched.start()


app = Flask(__name__)


@app.route('/', methods=['POST'])
def send_message():
    sid = os.environ['TWILIO_SID']
    token = os.environ['TWILIO_TOKEN']
    client = Client(sid, token)

    message = client.messages.create(
        body="Remember to activate MyNextGen",
        from_='whatsapp:+14155238886',
        to='whatsapp:+573122354434'
    )


if __name__ == '__main__':
    app.run()
    print('App is running')
