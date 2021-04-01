from flask import Flask,render_template
import subprocess

app = Flask("harsh")


@app.route("/hello")
def myhello():
	date = subprocess.getoutput("date /t")
	return(date)


@app.route("/search")
def mysearch():
	return render_template("e.html")