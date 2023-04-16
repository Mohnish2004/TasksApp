from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite' # /// = relative path, //// = absolute path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # To ensure there are no warnings
db = SQLAlchemy(app)


class Todo(db.Model): # this is the database model, where we specify all entries for the database
    id = db.Column(db.Integer, primary_key=True) # This database needs 3 things, id, to do title and boolean value to know if its completed 
    title = db.Column(db.String(100)) # straight forward strng for title with max characters 100
    description = db.Column(db.String(200))
    complete = db.Column(db.Boolean) # boolean value to check completion
    status = db.Column(db.Integer) # EXPERIMENTAL TO ADD STATUS SLIDER
    due_date = db.Column(db.Date)
    priority = db.Column(db.String(10))
    due_date = db.Column(db.DateTime)  # Change the due date column to a DateTime type



@app.route("/")
def landing():
    return render_template("Landing.html") 



@app.route("/index")
def index():
    todo_list = Todo.query.all() # shows all tasks
    return render_template("base.html", todo_list=todo_list) # flask depends on jinja engine which is used in html file


@app.route("/add", methods=["POST"])# this array is a post method, need to learn it
def add():
    title = request.form.get("title")
    description = request.form.get("description")
    due_date_str = request.form.get("due_date") + " " + request.form.get("due_time")  # Concatenate date and time strings
    priority = request.form.get("priority")
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M")  # Convert the concatenated string to a datetime object

    new_todo = Todo(title=title, description=description, complete=False, due_date=due_date, priority=priority)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/update/<int:todo_id>") # this is different because its for an integer id 
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() # we are not just requested but instead querying/searching for the update function. THe first is to return just one
    todo.complete = not todo.complete # changes boolean value
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/status/<int:todo_id>", methods=["POST"]) # this is different because its for an integer id 
def status(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first() # we are not just requested but instead querying/searching for the update function. THe first is to return just one
    todo.status = int(request.form["status"]) # changes depending on slider
    db.session.commit()
if __name__ == "__main__":
    with app.app_context(): # creates context for DB to be created
        db.create_all() # creates database - this resulted in database file being created 
    app.run(debug=True)