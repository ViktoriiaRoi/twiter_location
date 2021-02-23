from flask import Flask, render_template, request
import location
import build_map

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find_location", methods=["POST"])
def find_location():
    username = request.form.get("username")
    bearer = request.form.get("bearer")

    if not username or not bearer:
        return render_template("empty.html")
    
    friends_location = location.main(username, bearer)
    if not friends_location:
        return render_template("failure.html")

    
    build_map.main(friends_location)
    return render_template("Friends_map.html")

if __name__ == '__main__':
    app.run(debug=True)