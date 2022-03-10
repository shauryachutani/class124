from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title' : 'Buying groceries',
        'description': 'Milk, cheese, veggies',
        'done': False
    },
    {
        'id': 2,
        'title': "Learn python",
        'description': 'Searching for good tutorials',
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/add-data",methods = ["POST"])
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide data"
        }, 400)
    task={
        "id":tasks[-1]['id']+1,
        "title":request.json["title"],
        "description":request.json.get("description", ""),
        "done":False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":'task added succsessfully'
    })

@app.route("/get-data")

def getTask():
    return jsonify({
        "data":tasks
    })




if(__name__ == "__main__"):
    app.run(debug = True)

#Get Method - request data from a source
#Post Method - to send data to a server - create multiple copies of the same data
#Put Method - sent data to a server - Only one copy
#Delete method - deleting a resource
