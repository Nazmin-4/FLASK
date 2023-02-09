from flask import Flask,render_template,request,session,redirect
from mysql.connector import connect
con=connect(host='localhost',port=3306,database='mysql' #database name
,user='root')
# cur=con.cursor()
# cur.execute("insert into CSE values('nazmin',2),('hema',3)")
# cur.execute("insert into CSE values('sravani',4)")
# con.commit()
myapp=Flask(__name__)
myapp.secret_key="kjhgfds"
@myapp.route("/")
def regg():
    return render_template("reg.html")

@myapp.route("/home")
def hi():
    return redirect("/login")
@myapp.route("/index")
def hello():
    return render_template("index.html")
@myapp.route("/about")
def about():
    return "hello nazuu"
@myapp.route("/name/<string:id>")
def name(id):
    return "hELLO "+id #dynamic urls

@myapp.route("/myform",methods=["GET","POST"])
def myform():
    if request.method=="POST":
        user=request.form["name"]
        password=request.form["password"]
        rpass=request.form["rpassword"]
        if password==rpass:
            cur=con.cursor()
            cur.execute("insert into reg values(%s,%s)",(user,rpass))#dynamic values
            con.commit()
            # return "success"
            return render_template("myform.html",msg="successfully registered")
        else:
            return "bad credentials"
    else:
        return "get request"
@myapp.route("/login",methods=["GET","POST"])
def log():
    if 'name' in session: #if session["name"] or session.get("name")
        return render_template("myform.html",msg=session["name"])
    else:
        if request.method=="POST": 
            user=request.form["name"]
            password=request.form["password"]
            cur=con.cursor()
            session["name"]=user
            cur.execute("Select * from reg where name=%s and password=%s",(user,password))
            a=cur.fetchone()
            print(a)
            if a is not None:
                return render_template("myform.html",msg=user)
            else:
                return "user not found"
        else:
            # return "get request"
            if 'name' in session:
                return render_template("myform.html",msg=session["name"])
            else:
                return "Get Request"

@myapp.route("/logout")
def logout():
    session.clear()
    return "logged out"
if __name__=="__main__":
    myapp.run(debug=True)