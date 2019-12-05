#! /usr/bin/env python3.7

import json
import os
import random
import time

import requests
from slacker import Slacker
# credentials will be your oauth slack token for your workspace
import credentials as creds

slack_api_token = creds.bot_token
web_hook_url = creds.hook_url
slack = Slacker(slack_api_token)


def night_dinner_shuffle():
  """ This is meant to shuffle through your list of teammates 
      or department members to decide who gets to recommend a place for dinner """
    while True:
        noc_list = ["list of teammates"]
        random.shuffle(noc_list)
        sod = noc_list[0]
        print(sod)
        rerun = input("Do you want to run again? Y / N \n")
        if rerun == 'Y' or 'y':
            continue
        else:
            print("Posting to Slack!")
            chosen_sod = {'text' : "This person gets to choose dinner this week! "}
            sod = {'text' : " %s " % (sod)}
            requests.post(web_hook_url,data=json.dumps(chosen_sod))
            requests.post(web_hook_url,data=json.dumps(sod))
            break 

night_dinner_shuffle()
