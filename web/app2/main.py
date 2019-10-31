from flask import Flask
from flask import render_template


app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")


@app.route("/cms")
def cms():
    return render_template("cms.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/category")
def category():
    return render_template("category.html")


@app.route("/productpage")
def productpage():
    return render_template("productpage.html")

@app.route("/howitworks")
def howitworks():
    return render_template("howitworks.html")


@app.route("/about-us")
def about_us():
    return render_template("about-us.html")

if __name__ == '__main__':
    app.run(debug=True)
