import urllib.request
import json
import os
from flask import Flask, request
app = Flask(__name__)

from bs4 import BeautifulSoup
sessionStorage = {}

@app.route("/", methods =['post'])
def main():

    response = {


            "version":request.json['version'],
            "session": request.json['session'],
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


    lleng = 1024


    while lleng >= 1024: # remove for speed but u need to slice pasta
            paste = urllib.request.urlopen("https://pastach.ru/p/random")

            pst = paste.read()

            out = pst.decode("utf8")

            html = BeautifulSoup(out, features="html.parser")
            lleng = len(html.article.section.text)
            print(lleng)
            #pasta = html.article.section.text[:1024].replace("\n"," ")
            pasta = html.article.section.text.replace("\n"," ")
    return pasta

if __name__ == '__main__':

    app.run(port=5000)
    print(getPaste())

