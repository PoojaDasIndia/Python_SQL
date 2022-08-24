from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        num1 = request.json["number1"]
        num2 = request.json["number2"]
        result = num1 + num2
        return jsonify(str(result))


if __name__ =="__main__":
    app.run()

