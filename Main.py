import urllib.request
from http.server import *
import json
import logging
from flask import Flask, request
app = Flask(__name__)

from bs4 import BeautifulSoup
sessionStorage = {}

@app.route("/", methods =['post'])
def main():

    response = {

            "version":"1.0",
            # "version":request.json['version'],
            # "version": request.json['session'],
            "response": {
                "end_session": False
            },



    }
    handle_dialog(response,request.json)
    return json.dumps(response,ensure_ascii=False,indent=2)
def handle_dialog(res,req):
    if req['request']['command'] == "расскажи пасту":
        ## Проверяем, есть ли содержимое
        res['response']['text'] = getPaste()
    else:
        ## Если это первое сообщение — представляемся
        res['response']['text'] = """Я пастабот, скажи:"расскажи пасту" и я расскажу тебе пасту с уютного или двача """


def getPaste():
    paste = urllib.request.urlopen("https://pastach.ru/p/random")
    pst = paste.read()

    out = pst.decode("utf8")

    html = BeautifulSoup(out, features="html.parser")

    pasta = html.article.section.text[:1024].replace("\n"," ")
    return pasta
app.run(port=80)