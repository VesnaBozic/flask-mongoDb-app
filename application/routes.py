from application import app
from flask import render_template, request, json, Response

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

@app.route("/register")
def register():
    return render_template("register.html", register= True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)

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



