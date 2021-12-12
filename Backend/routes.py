from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from Backend import app, db
from Backend.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from Backend.forms import TaskCreatorForm, TaskDetailForm, TaskFilterForm
from DBHandler.models import User, Task
from Backend.email import send_password_reset_email

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    tasks = User.allTask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travel'))
        if form.movie.data:
            return redirect(url_for('movie'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route('/index/online_meetings', methods=['GET', 'POST'])
@login_required
def online_meetings():
    tasks = User.onlinemeetingstask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travel'))
        if form.movie.data:
            return redirect(url_for('movie'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route('/index/projects', methods=['GET', 'POST'])
@login_required
def projects():
    tasks = User.projectstask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travel'))
        if form.movie.data:
            return redirect(url_for('movie'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route('/index/movie', methods=['GET', 'POST'])
@login_required
def movie():
    tasks = User.movietask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travel'))
        if form.movie.data:
            return redirect(url_for('movie'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)


@app.route('/index/birthday', methods=['GET', 'POST'])
@login_required
def birthday():
    tasks = User.birthdaytask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travel'))
        if form.movie.data:
            return redirect(url_for('movie'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)


@app.route('/index/others', methods=['GET', 'POST'])
@login_required
def others():
    tasks = User.othertask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travel'))
        if form.movie.data:
            return redirect(url_for('movie'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, first_name=form.first_name.data
            ,last_name=form.last_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)

@app.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskCreatorForm()
    if form.validate_on_submit():
        task = Task(creator=current_user, title=form.title.data, task_type=form.task_type.data)
        db.session.add(task)
        db.session.commit()
        flash('Task successfully created!! Add few more details')
        return redirect(url_for('edit_task'))
    return render_template('create_task.html', title='Create Task', form=form)

@app.route('/edit_task/<task>', methods=['GET', 'POST'])
@login_required
def edit_task():
    form = TaskDetailForm()
    if form.validate_on_submit():
        flash('Task detail updated!!')
        return redirect(url_for('index'))
    elif request.method == 'GET':
        form.date.data = datetime.now()
        form.time.data = datetime.now()
    return render_template('task_detail.html', title='Edit Task', form=form)

@app.route('/delete_task/<title>', methods=['GET','POST'])
@login_required
def delete_task(title):
    task = Task.query.filter_by(title=title).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

