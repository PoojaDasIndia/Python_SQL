# Importing libraries  which we use for our App ,Database using (MySQL, SQL Server, MongoDB)
from flask import Flask, request, jsonify
import mysql.connector as con

# creating object for Flask
app = Flask(__name__)


# MySQL Connection

mysqldb = con.connect(
    host='localhost',
    user='root',
    password='poojadas1993',
    database='TaskAPI'
)
# creating cursor
cur = mysqldb.cursor()


# query="CREATE TABLE TaskAPI (Roll_No INT PRIMARY KEY, Name VARCHAR(50))"
# cur.execute(query)
# print("Table Created!!")
# mysqldb.close()

@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        Roll_no = request.json['Roll_no']
        Name = request.json['Name']
        query = f"INSERT INTO TaskAPI VALUES ({Roll_no},'{Name}')"
        cur.execute(query)
        mysqldb.commit()
        return jsonify(str("Insertion Complete"))


@app.route("/select", methods=["GET"])
def select():
    if request.method == "GET":
        query = "SELECT * FROM TaskAPI"
        cur.execute(query)
        result = cur.fetchall()
        return jsonify(str(result))

@app.route("/update", methods=["POST"])
def update():
    if request.method == "POST":
        Roll_no = request.json['Roll_no']
        Name = request.json['Name']
        query = f"UPDATE TaskAPI SET Name ='{Name}' where Roll_no ={Roll_no}"
        cur.execute(query)
        return jsonify(str("Update Successfully"))


if __name__ == "__main__":
    app.run()
