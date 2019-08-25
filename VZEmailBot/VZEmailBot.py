#! /usr/bin/env python3
import os
import schedule
import time
import requests
import json
import credentials as creds
from slacker import Slacker


slack_api_token = creds.bot_token
web_hook_url = 'your_webhook_url'
slack = Slacker(slack_api_token)
slack_msg = {'text': 'VZ email script activated!'}
four = {'text': 'Running 4pm daily email task'}
two = {'text': ' Running Mon 2am email task'}
twopm = {'text': 'Running Mon 2pm email task'}

#Request would post that script was ran successfully
requests.post(web_hook_url,data=json.dumps(slack_msg))

def job():
    requests.post(web_hook_url,data=json.dumps(four))
    #Post to slack channel that job at 4 PM task is running
    os.system('path/to/shell/script')
    #Post output that was redirected form stdout to text file to slack channel
    slack.files.upload('emailscript.txt', channels=['dest_channel_id'])

def job1():
    requests.post(web_hook_url,data=json.dumps(two))
    #Post to slack channel that 2 AM task is running
    os.system('path/to/shell/script)')
     #Post output that was redirected form stdout to text file to slack channel
    slack.files.upload('mon_weekly_start.txt', channels=['dest_channel_id'])

def job2():
    requests.post(web_hook_url,data=json.dumps(twopm))
    os.system('/path/to/shell/script')
     #Post output that was redirected form stdout to text file to slack channel
    slack.files.upload('mon_weekly_complete.txt', channels=['dest_channel_idJ'])

#Use schedule module to have python script run at specified times
schedule.every().day.at("16:01").do(job)
schedule.every().monday.at("02:00").do(job1)
schedule.every().monday.at("14:00").do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)
