import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, StudentProfile, Course
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


#db_drop_and_create_all()

# ROUTES


@app.route('/students', methods=['GET'])
def get_drinks():
    students = StudentProfile.query.all()

    return jsonify({
        'success': True,
        'students': [student.short() for student in students]
    }), 200



@app.route('/students/<int:student_id>', methods=['GET'])
def get_drink_detail(payload):
    try:
          student = StudentProfile.query.get(student_id)

          if student is None:
                abort(404)
          
                 
          return jsonify({
            "success": True,
            "student": student,
          }), 200
    except:
        abort(422)


    

@app.route('/students', methods=['POST'])
def new_student_profile():
    try:
        body = request.get_json()

        name = body.get('name')
        semester = body.get('semester')
        status = body.get('status')
        proficient_subs = body.get('proficient_subs')
        image_link = body.get('image_link', None)
        seeking_help_description = body.get('seeking_help_description', None)
        seeking_help = body.get('seeking_help', None)
        course = body.get('course', None)

        
        new_student_profile = StudentProfile.filter(StudentProfile.name == str(name)).all()

        return ({
                "success": True,
                "student": new_student_profile
        }), 200

    except:
            abort(422)





    

@app.route('/student-status/<int:id>', methods=['PATCH'])
def update_status(payload, id):
    req = request.get_json()
    course = Course.query.filter(StudentProfile.student_id == req['id']).one_or_none()

    if not course:
        abort(404)

    try:
        course_name = req.get('course')
        course_status = req.get('status')
        if course_name:
            course.course_name = course_status

        if course_status:
            course.course_name = json.dumps(req['course'])

        StudentProfile.update()
    except BaseException:
        abort(400)

    return jsonify({'success': True, 'courses': [course.long()]}), 200





# Error Handling


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422




@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404




@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": 'Unathorized'
    }), 401


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": 'Internal Server Error'
    }), 500


@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": 'Bad Request'
    }), 400


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": 'Method Not Allowed'
    }), 405

