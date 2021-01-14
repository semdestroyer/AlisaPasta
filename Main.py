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
    paste = urllib.request.urlopen("https://pastach.ru/p/random")
    pst = paste.read()

    out = pst.decode("utf8")

    html = BeautifulSoup(out, features="html.parser")

    pasta = html.article.section.text[:1024].replace("\n"," ")
    return pasta
#app.run( port=int(os.environ.get('PORT', 5000)))
if __name__ == '__main__':
    #app.run()
    app.run(port=int(os.environ.get('PORT', 5000)))