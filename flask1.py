from flask import Flask, redirect, url_for

# Creating instance of flask application

app = Flask(__name__)

@app.route("/")  # Creates the default link for home page
def home_page():
    return "This is the main home Page<h1>Hello<h1/>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home_page"))



if __name__ == "__main__":
    app.run()
