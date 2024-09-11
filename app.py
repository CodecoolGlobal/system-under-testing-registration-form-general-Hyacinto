import functools

import bcrypt
from flask import Flask, render_template, request, session, redirect, url_for

import data_manager

USERNAME_KEY = 'username'

app = Flask(__name__)
app.secret_key = bcrypt.gensalt()
data_manager.init_data()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not is_logged_in():
            return redirect(url_for('login'))
        return view(**kwargs)

    return wrapped_view


@app.get('/register')
def registration_page():
    return render_template('register.html')


@app.post('/register')
def register():
    user_data = request.form.to_dict()
    data_manager.add_user(user_data)
    return redirect_to_landing_page()


@app.get('/')
def landing():
    if is_logged_in():
        return redirect(url_for('list_students'))
    else:
        return redirect(url_for('login_page'))


@app.get('/login')
def login_page():
    if is_logged_in():
        return redirect_to_landing_page()
    return render_template('login.html')


@app.post('/login')
def login():
    if is_logged_in():
        return redirect_to_landing_page()
    login_data = request.form.to_dict()
    validation_result = data_manager.check_login(login_data)
    if validation_result:
        session[USERNAME_KEY] = login_data["username"]
        return redirect_to_landing_page()
    else:
        return render_template('login.html', after_unsuccessful=True)


@app.get('/logout')
@login_required
def logout():
    session.pop(USERNAME_KEY)
    return redirect_to_landing_page()


@app.get('/add')
@login_required
def form():
    return render_template('student-form.html')


@app.post('/add')
@login_required
def add_student():
    data = request.form.to_dict()
    data_manager.add_student(data)
    return render_template('student-form.html', added_student_email=data["email"])


@app.get('/list')
@login_required
def list_students():
    data = data_manager.read_students()
    return render_template('student-list.html', data=data)


def is_logged_in():
    return USERNAME_KEY in session


def redirect_to_landing_page():
    return redirect(url_for("landing"))


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5555
    )
