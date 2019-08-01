#! /usr/bin/env python3
import os
import schedule
import time
import requests
import json
import credentials as creds
from slacker import Slacker


slack_api_token = creds.bot_token
web_hook_url = 'https://hooks.slack.com/services/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'
slack = Slacker(slack_api_token)
slack_msg = {'text': 'VZ email script activated!'}
four = {'text': 'Running 4pm daily email task'}
two = {'text': ' Running Mon 2am email task'}
twopm = {'text': 'Running Mon 2pm email task'}

requests.post(web_hook_url,data=json.dumps(slack_msg))

def job():
    requests.post(web_hook_url,data=json.dumps(four))
    os.system('sh /Users/christopher.abidog/workspace/noc/VZEmailBot/emailscript.sh')
    slack.files.upload('emailscript.txt', channels=['CLGCXUSPJ'])

def job1():
    requests.post(web_hook_url,data=json.dumps(two))
    os.system('sh /Users/christopher.abidog/workspace/noc/VZEmailBot/mon_weekly_start.sh)')
    slack.files.upload('mon_weekly_start.txt', channels=['CLGCXUSPJ'])

def job2():
    requests.post(web_hook_url,data=json.dumps(twopm))
    os.system('sh /Users/christopher.abidog/workspace/noc/VZEmailBot/mon_weekly_complete.sh)')
    slack.files.upload('mon_weekly_complete.txt', channels=['CLGCXUSPJ'])


schedule.every().day.at("16:01").do(job)
schedule.every().monday.at("02:00").do(job1)
schedule.every().monday.at("14:00").do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)
