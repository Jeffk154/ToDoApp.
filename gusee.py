import flask
import random
correctnumber = random.randint(0,100)
app = flask.Flask("myawesomeapp")
@app.route("/homepage")
def home():
    return flask.render_template("homepage.html")


@app.route("/about")
def about():
    return flask.render_template("about.htm")

@app.route("/LOG", methods=["GET", "POST"])
def Log():
    if flask.request.method == "POST":
        print("You Have A New Login")
        name = flask.request.form["UserName"]
        Pass = flask.request.form["Password"]
        print(name + Pass)
    return flask.render_template("LOGIN.htmL")

@app.route("/gusee", methods=["GET", "POST"])
def gusee():
    if flask.request.method == "POST":    
        print("Check Number")
        guseednumber = flask.request.form.get("number")
        print(guseednumber)
        
        if int (guseednumber) == correctnumber:
            return("You Guessed The Number")
        if int (guseednumber) > correctnumber:
            return "TO HIGHHHHH TRY AGIN"
        if int (guseednumber) < correctnumber:
            return "TO LOWWWWW TRY AGAIN"
    return flask.render_template("Gusee.html")


app.run()