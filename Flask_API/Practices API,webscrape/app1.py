from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/abc", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        num1 = request.json["num1"]
        num2 = request.json["num2"]
        num = num1 + num2
        return jsonify((str(num)))


if __name__ == "__main__":
    app.run(port=5002)
