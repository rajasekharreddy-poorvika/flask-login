from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_required,login_user,logout_user,current_user,UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sample.db"
app.config['SECRET_KEY'] = "DFDSFDSFAF"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'signin'




class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(322))
    name = db.Column(db.String(322))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return "Home page"

@app.route("/create")
def create():
    db.create_all()
    return "Database is created"
@app.route("/delete")
def delete():
    db.drop_all()
    return "Database was deleted"

@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method =="POST":
        email = request.form['email']
        name = request.form['name']
        new_value = User(email=email,name=name)
        db.session.add(new_value)
        db.session.commit()
        return "Values are insert into database"
    return render_template("home.html")

@app.route("/signin",methods=['GET','POST'])
def signin():
    if request.method=="POST":
        name = request.form['name']
        user = User.query.filter_by(name = name).first()
        if user:
            login_user(user)
            current_user.active = True
            return redirect(url_for('home'))
        else:
            return "User dont have in database"
    else:
        return render_template("signin.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "You are now logout"

@app.route("/cuser")
@login_required
def curr():
    return "The current user" + current_user.name

@app.route("/dashboard")
@login_required
def dashboard():
    return "You are login in Dashboard"




if __name__=='__main__':
    app.run(debug=True)
