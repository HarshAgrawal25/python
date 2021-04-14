from flask import Flask
from flask import render_template
from flask import request
import subprocess
app = Flask("myapp")


@app.route("/cmd")
def cmd():
	form  = render_template("form.html")
	return form 

@app.route("/run", methods=["GET"])
def run(): 
	cmd = request.args.get("x")
	print("Harsh Agrawal")
	return "<pre>"+ subprocess.getoutput(cmd) +"</pre>" 

app.run(debug=True, port=5555)
	