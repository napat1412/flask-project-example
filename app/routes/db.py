from flask import Blueprint
from app import db
from flask import Flask, g, request, flash, url_for, redirect, render_template
from app.models.Students import students
import json

api_db = Blueprint('api_db', __name__)

@api_db.route("/student")
def show_all():
  print(students.query.all())
  return render_template('show_all.html', students = students.query.all() )

@api_db.route('/student-new', methods = ['GET', 'POST'])
def new():
  if request.method == 'POST':
    print('In Post')
    if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         print('Please enter all the fields')
         flash('Please enter all the fields', 'error')
    else:
      student = students(name=request.form['name'], city=request.form['city'],
                         addr=request.form['addr'], pin=request.form['pin'])
      print('Record was received')
      db.session.add(student)
      db.session.commit()
      print('Record was successfully added')
      flash('Record was successfully added')
      return redirect(url_for('api_db.show_all'))
  return render_template('new.html')
  
@api_db.route('/student/<string:name>', methods=['GET'])
def get_student(name):
  student = students.query.filter_by(name=name).first()
  print(vars(student))
  result = {}
  result['id'] = student.id
  result['name'] = student.name
  result['city'] = student.city
  result['addr'] = student.addr
  result['pin'] = student.pin
  return json.dumps(result)
  
@api_db.route('/student/<string:name>', methods=['DELETE'])
def delete_student(name):
  student = students.query.filter_by(name=name).first()
  result = {}
  result['id'] = student.id
  result['name'] = student.name
  result['city'] = student.city
  result['addr'] = student.addr
  result['pin'] = student.pin
  db.session.delete(student)
  db.session.commit()
  return json.dumps(result)