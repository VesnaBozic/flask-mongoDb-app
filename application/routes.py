from application import app, db
from flask import render_template, request, json, Response, redirect,flash
from application.models import User,Course, Enrollment
from application.forms import LoginForm, RegisterForm


classes = [ {"courseID":"1111","title":"PY 101","description":"Intro to Python","credits":3,"term":"Fall, Spring"},
                {"courseID":"2222","title":"Flask 1","description":"Intro to Flask","credits":4,"term":"Spring"}, 
                {"courseID":"3333","title":"Int Py 201","description":"Intermediate Python Programming","credits":3,"term":"Fall"},
                {"courseID":"4444","title":"Adv F","description":"Advanced Flask","credits":3,"term":"Fall, Spring"}, 
                {"courseID":"5555","title":"FS","description":"Flask Security","credits":4,"term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index = True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Spring 2022"):

    # print(courses)
    return render_template("courses.html",  classes = classes, course = True, term = term)

@app.route("/register", methods=['GET', 'POST'])
def register():
    registration = RegisterForm()
    return render_template("register.html",registration=registration, register= True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get("email") == "test@flask.com":
            flash("You are logged in!", "success")
            return redirect("/index")
        else:
            flash("Something went wrong! Try again!", "danger")
    return render_template("login.html",title = "Login", form = form, login=True)

@app.route("/enrollment", methods =["GET", "POST"])
def enrollment():
    #THIS IS FOR GET METHOD
    # id = request.args.get('courseID')
    # title = request.args.get('title')
    # term = request.args.get('term')

    #THIS IS FOR POST
    id = request.form.get('courseID')
    title = request.form.get('title')
    term = request.form.get('term')

    return render_template("enrollment.html", enrollment=True, course = {"id": id, "title":title, "term" : term})

@app.route("/api/")
@app.route("/api/<index>")
def api(index=None):
    if (index == None):
        jdata = classes
    else:
        jdata = classes[int(index)]

    return Response(json.dumps(jdata), mimetype = "application\json")



@app.route("/user")
def user():
    # User(user_id=1, first_name="Vesna", last_name="Bozic", email="86veja@gmail.com", password="vesna").save()
    # User(user_id=4, first_name="Vaso", last_name="Boz", email="vaso@gmail.com", password="vaso").save()
    # User(user_id=5, first_name="Ana", last_name="Anic", email="ana@gmail.com", password="ana").save()
     users = User.objects.all()
     print(users)
     return render_template("user.html", users=users)









