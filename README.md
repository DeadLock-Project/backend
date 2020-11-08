# Backend for Peer2Peer App

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

Another one for easiness is Anaconda environement. Create Python 3.7 conda environment for this project. I have used and tested conda  environment.

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

Dependencies might show some conflicts, for any queries, start an issue. Preferrably the dependencies must be installed over mentioned environment, otherwise, will lead to WHEEL_BUILD_ERROR.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.


## Running the server

From within the `./` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.



## API Endpoints

```'/students', methods=['GET']```

    {
        'success': True,
        'students': [student.short() for student in students]
    }, 200


```'/students/<int:student_id>', methods=['GET']```

          {
            "success": True,
            "student": student,
          }, 200
    


    

```'/students', methods=['POST']```
    

        {
                "success": True,
                "student": new_student_profile
        }, 200






```'/student-status/<int:id>', methods=['PATCH']```

    {'success': True, 'courses': [course.long()]}, 200

