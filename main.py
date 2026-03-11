import flask

AllTasks = ["Ride Bicycle" , "Play Hide And" , "Sleep"]

app = flask.Flask("ToDoApp")

@app.route("/viewtasks" , methods=["GET" , "POST"])
def viewtask():
    if flask.request.method == "POST":
        print("Deleted Task")
        deltask = flask.request.form["DeleteTask"]
        AllTasks.remove(deltask)
    return flask.render_template("todo.html" , AllTasks = AllTasks)

@app.route("/Addtask", methods=["GET", "POST"])
def AddTask():
    if flask.request.method == "POST":
         print("New Task Added")
         Task = flask.request.form["AddTask"]
         print(Task)
         AllTasks.append(Task)
    return flask.render_template("addtask.html")





