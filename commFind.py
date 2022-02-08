from flask import Flask, render_template

commentsFinder = Flask(__name__)

@commentsFinder.route("/")
def home():
    return render_template("home.html",title="Home",custom_css="home")

@commentsFinder.route("/about")
def about():
    return render_template("about.html",title="About",custom_css="about")

@commentsFinder.route("/contact")
def contact():
    return render_template("contact.html",title="Contact",custom_css="contact")

if __name__ == "__main__":
    commentsFinder.run(debug=True)
