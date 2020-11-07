import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json


database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()





class StudentProfile(db.Model):
    __tablename__ = 'student'

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String)
    semester = Column(String(120))
    status = Column(String(120))
    proficient_subs = Column(db.ARRAY(String(120)))
    image_link = Column(String(500))
    seeking_help_description = Column(String(120))
    seeking_help = Column(db.Boolean)
    course = db.relationship('Course', backref="student", lazy=True)

    def __init__(self, name, semester, status, proficient_subs, image_link,seeking_help, seeking_help_description, course):
        self.name = name
        self.course = course
        self.semester = semester
        self.status =  status
        self.image_link= image_link
        self.proficient_subs = proficient_subs
        self.seeking_help = seeking_help
        self.seeking_help_description = seeking_help_description


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())

    def format(self):
        return {
      'id': self.id,
      'name': self.name,
      'course': self.course,
      'semester': self.semester,
      'status': self.status,
      'image_link': self.image_link,
      'proficient_subs': self.proficient_subs,
      'seeking_help': self.seeking_help,
      'seeking_help_description': self.seeking_help_description
    }



class Course(db.Model):
    __tablename__= 'course'

    id = Column(Integer(), primary_key=True)
    ds = Column(String(), nullable= False)
    dcs = Column(String(), nullable= False)
    maths= Column(String(), nullable= False)
    oop= Column(String(), nullable= False)
    systems= Column(String(), nullable= False)
    os = Column(String(), nullable= False)
    student_id = Column(Integer(), db.ForeignKey('student.id'), nullable=False)


    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def __repr__(self):
        return json.dumps(self.short())

    def long(self):
        return {
      'id': self.id,
      'ds': self.ds,
      'dcs': self.dcs,
      'maths': self.maths,
      'oop': self.oop,
      'systems': self.systems,
      'os': self.os,
      'student_id': self.student_id
      }

