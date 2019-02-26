#coding=utf-8
import requests
import tempfile
import os

import re
import random
import time
import datetime
#from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort
import sqlite3
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.exceptions import LineBotApiError
from linebot.models import *
from bs4 import BeautifulSoup
app = Flask(__name__)
#bear
'''
line_bot_api = LineBotApi('cRMF7+DwEKVhAwHC0EB7oBQqtEZ09thaY6hLFnIrKy25hE385Al8RoxMxTN+VCsdYOIjGDwpLqXoxR60gdIvithhKyaSXgUBYL2V8k+/aDS//tdw4wk578xqutoHJEdLJxL9GkRKFZ0M8VbSHiDC5gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9b57c56f50bb020a8eda208c96b2c59c')
'''
#nini

line_bot_api = LineBotApi('/gYOVdyGfdrePeWzKes5zWkvwlJ42148waHkXu4/V4wdwlfgFHh1TcBNKvLYjvLUf2jkJ0SJ3TPK0eZ8s+wIec+kPjmrN9H7S5c+EonV4T5GK5/eo+uZLL1vcp1VgmCU0EL6kk2nmiKd7Ce7nVdSkAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d6c704bba551d5e05c71b8694416e89a')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MemberJoinEvent)
def handle_memberJoined(event):
    print(event)

if __name__ == '__main__':
#    app.run(host='0.0.0.0',port=5000)
    app.run(port=5001)
    #app.run(host='0.0.0.0',port=5000,ssl_context=context)

#    app.run()
