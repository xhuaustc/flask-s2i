from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "HELLO WORLD APP"


app.run(host='0.0.0.0', debug=False)
