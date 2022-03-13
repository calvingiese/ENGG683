from urllib import request
from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)

# Credentials to access app
user_credentials = {'user1': 'abc', 'user2': '123'}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in user_credentials and password == user_credentials[username]:
            # Persist session information as needed
            session["username"] = username
            return redirect(url_for("search"))
        else:
            return render_template("login_error.html")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)