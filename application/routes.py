from application import app, db
from flask import render_template, request, json, Response, redirect,flash, url_for, session
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

# first I used data from list of dictionaries, but later switch to database, this won't be used anymore
# classes = [ {"courseID":"1111","title":"PY 101","description":"Intro to Python","credits":3,"term":"Fall, Spring"},
#                 {"courseID":"2222","title":"Flask 1","description":"Intro to Flask","credits":4,"term":"Spring"}, 
#                 {"courseID":"3333","title":"Int Py 201","description":"Intermediate Python Programming","credits":3,"term":"Fall"},
#                 {"courseID":"4444","title":"Adv F","description":"Advanced Flask","credits":3,"term":"Fall, Spring"}, 
#                 {"courseID":"5555","title":"FS","description":"Flask Security","credits":4,"term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index = True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term=None):
    if term is None:
        term = "Spring 2022"
    classes = Course.objects.order_by("+courseID") #with order_by we are sorting courses + asc order, - desc, default asc 
    return render_template("courses.html",  classes = classes, course = True, term = term)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))
    registration = RegisterForm()
    if registration.validate_on_submit():
        user_id    =  User.objects.count() #this count number of objects in database
        user_id   +=  1

        email      = registration.email.data
        password   = registration.password.data
        first_name = registration.first_name.data
        last_name  = registration.last_name.data

        #when we got all data from registration form we save it in database
        user = User(user_id=user_id, email=email, password=password, first_name=first_name, last_name=last_name)
        #we hash password
        user.set_password(password)
        #and then we save it
        user.save()
        flash("You are succesfully registered", "sucess")
        return redirect(url_for('index'))
    return render_template("register.html",title="Register",registration=registration, register= True)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        email    =   form.email.data
        password =   form.password.data
   
        user = User.objects(email=email).first() #we are comparing email from form with email in database, first means that it returns a single object of this user
        if user and user.get_password(password): #validating password, password is hashed
      
            #flashing system is Flask way to give feedback to a user
            #flashing with categories we use to display success or danger message
            flash(f"{user.first_name}, You are logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Something went wrong! Try again!", "danger")
    return render_template("login.html",title = "Login", form = form, login=True)

@app.route("/logout")
def logout():
    #ending session
    session['user_id'] = False
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route("/enrollment", methods =["GET", "POST"])
def enrollment():

    if session.get('username'):
        return redirect(url_for('login'))
     
    courseID = request.form.get('courseID')
    course_title = request.form.get('title')
   
    user_id = session.get('user_id')

    if courseID:
        if Enrollment.objects(user_id=user_id,courseID=courseID):
            flash(f"You are already enrolled in the {course_title}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id,courseID=courseID).save()
            flash(f"You are now enrolled in the {course_title}!", "success")

    classes = list(User.objects.aggregate(*[
            {
                '$lookup': {
                    'from': 'enrollment', 
                    'localField': 'user_id', 
                    'foreignField': 'user_id', 
                    'as': 'r1'
                }
            }, {
                '$unwind': {
                    'path': '$r1', 
                    'includeArrayIndex': 'r1_id', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$lookup': {
                    'from': 'course', 
                    'localField': 'r1.courseID', 
                    'foreignField': 'courseID', 
                    'as': 'r2'
                }
            }, {
                '$unwind': {
                    'path': '$r2', 
                    'preserveNullAndEmptyArrays': False
                }
            }, {
                '$match': {
                    'user_id': user_id
                }
            }, {
                '$sort': {
                    'courseID': 1
                }
            }
]))
    term = request.form.get('term')
    return render_template("enrollment.html", title="Enrollment", enrollment=True, classes=classes)

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
    # here we created instances of User for testing purpose, won't use it anymore
    # User(user_id=1, first_name="Vesna", last_name="Bozic", email="86veja@gmail.com", password="vesna").save()
    # User(user_id=4, first_name="Vaso", last_name="Boz", email="vaso@gmail.com", password="vaso").save()
    # User(user_id=5, first_name="Ana", last_name="Anic", email="ana@gmail.com", password="ana").save()
     users = User.objects.all()
     print(users)
     return render_template("user.html", users=users)









