from flask import Flask
app= Flask("myiiec")
 
@app.route('/form')
def myform():
	return "form-harsh"

@app.route('/data')
def mydata():
	return "data-harsh"
app.run(port=5555, debug=True)