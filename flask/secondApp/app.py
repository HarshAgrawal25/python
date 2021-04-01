from flask import Flask
from flask import render_template
from flask import request

app = Flask("myapp")

@app.route("/") 
def home():
	print("Harsh")
	return "i am in home hello!!"

@app.route("/menu",methods =["GET"])
def myemnu():
	name = request.args.get("x")
	company = request.args.get("y")
	#name ="jack"
	
	htmlcode = render_template("mymenu.html",myname = name,cname= company)
	return htmlcode

@app.route("/form")
def form():
	form = render_template("myform.html")
	return form 