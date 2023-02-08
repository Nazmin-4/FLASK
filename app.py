from flask import Flask,render_template,request
from mysql.connector import connect
con=connect(host='localhost',port=3306,database='mysql' #database name
,user='root')
cur=con.cursor()
cur.execute("insert into CSE values('nazmin',2),('hema',3)")
cur.execute("insert into CSE values('sravani',4)")
con.commit()
myapp=Flask(__name__)
@myapp.route("/")
@myapp.route("/home")
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
        return render_template("myform.html",user=user)
    else:
        return "get request"
if __name__=="__main__":
    myapp.run(debug=True)