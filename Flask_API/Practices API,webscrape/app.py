from flask import Flask, request

app = Flask(__name__)


@app.route("/abc")
def enroll():
    name = request.args.get("name")
    roll = request.args.get("roll")
    return f"Your Name is {name} and Roll No. is {roll}"


if __name__ == "__main__":
    app.run(port=5001)
