from flask import Flask, render_template,jsonify,request
from wordcloud_html import word_cloud

app = Flask(__name__, template_folder="templates", static_folder='static')

title = "detecting COVID-19 misinformation in text-based social media posts."
footer = "This Single Page Application is powered by Flask and JQuery"



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# About Page Route
@app.route("/about")
def home():
    return render_template("index.html", title=title, footer=footer)

# Demo Input Route
@app.route("/demo-input")
def demo():
    return render_template("demo-input.html", title=title, footer=footer)

# Demo Output Route
@app.route("/demo-output")
def input():
    wc = word_cloud('userTweets.csv')
    return render_template("demo-output.html", title=title, footer=footer, wordcloud=wc)


@app.route('/returnjson', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = {
            "Modules" : 15,
            "Subject" : "Data Structures and Algorithms",
        }
  
        return jsonify(data)
