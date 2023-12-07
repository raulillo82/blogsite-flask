from flask import Flask, render_template
from datetime import datetime as dt
import requests

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html", year=dt.now().year)
    #return "Hello World!"

@app.route("/guess/<name>")
def greet(name):
    agify_api = "https://api.agify.io/"
    age_request = requests.get(url=agify_api, params={"name": name})
    age_request.raise_for_status()
    age = age_request.json()["age"]

    genderize_api = "https://api.genderize.io/"
    gender_request = requests.get(url=genderize_api, params={"name": name})
    gender_request.raise_for_status()
    gender = gender_request.json()["gender"]

    return render_template("guess.html", name=name.title(), gender=gender, age=age)

@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    #Run the app in debug mode and auto-reload
    app.run(debug=True)
