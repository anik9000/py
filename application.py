from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "How will I add something more?"
@app.route("/")
def hello2():
    return "Hi World!"
