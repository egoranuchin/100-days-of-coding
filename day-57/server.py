from flask import Flask, render_template
import random
import datetime
import requests

random_number = random.randint(1, 10)
now = datetime.datetime.now()
time_year = now.year

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1, 10)
    now = datetime.datetime.now()
    time_year = now.year
    name = "Egor Anuchin"
    return render_template("index.html", num=random_number, CURRENT_YEAR=time_year, MY_NAME=name)

@app.route('/guess/<name>')
def guess(name):
    name = name
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(url = gender_url)
    response.raise_for_status()
    data1 = response.json()
    gender = data1["gender"]
    age_url = f"https://api.agify.io?name={name}"
    response = requests.get(url=age_url)
    response.raise_for_status()
    data2 = response.json()
    age = data2["age"]

    return render_template("guess.html", NAME = name, GENDER = gender, AGE = age, CURRENT_YEAR=time_year, MY_NAME=name)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts = all_posts)


if __name__ == "__main__":
    app.run(debug=True)
