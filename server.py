from flask import Flask, render_template, request, redirect
from users import User
app = Flask(__name__)






@app.route("/")
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route("/create_user")
def createpage():
    return render_template("create_user.html")

@app.route("/edituser/<int:id>")
def updaterender(id):
    data = {
        "id" : id
    }
    users = User.get_one(data)
    return render_template("update.html", user = users)

@app.route("/read")
def readpage():
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)

@app.route("/read_one/<int:id>")
def readOnePage(id):
    data = {
        "id" : id
    }
    users = User.get_one(data)
    print(users)
    return render_template("read_one.html", user = users)



@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    User.save(data)
    return redirect('/read')

@app.route("/delete/<int:id>")
def delete_user(id):
    data = {
        'id' :id
    }
    User.delete_user(data)
    return redirect("/read")

@app.route("/update_user/<int:id>", methods = ["POST"])
def update_user(id):
    data = {
        'id' : id,
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form ["email"]
    }
    User.update_user(data)
    return redirect("/read")




if __name__ == "__main__":
        app.run(debug=True)

