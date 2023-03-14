from flask import Flask
from threading import Thread

app = Flask('')
#app = Flask(__name__, static_url_path='')

@app.route('/')
def home():
    return "<B>Hello. I am alive!</B>"
  #return app.send_from_directory("/", 'index.html')
  #return app.render_template("index.html")

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()