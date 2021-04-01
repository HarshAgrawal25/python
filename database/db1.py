from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask("iiecapp")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

db = SQLAlchemy(app)
print(db)

class IIEC(db.Model):
	id = db.Column(db.Integer , primary_key = True)
	name = db.Column(db.Text)
	age = db.Column(db.Integer)
	remarks = db.Column(db.Text)

	def __init__(self,name,age,remarks):
		self.name = name
		self.age = age
		self.remarks = remarks

db.create_all()

#create operation
""" 
tom = IIEC("jerry",20,"ok")
db.session.add(tom)
db.session.commit()
"""

#read operation
r2 = IIEC.query.get(2)
print(r2.name)

r1 = IIEC.query.all()
print(r1[0].name)

rn =IIEC.query.filter_by(age=20)
print(rn.all())


#update

r10 = IIEC.query.get(1)
r10.age = 15
db.session.add(r10)
db.session.commit()

#delete
rall = IIEC.query.get(2)
db.session.delete(rall)
db.session.commit()