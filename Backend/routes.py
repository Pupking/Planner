from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from Backend import app, db
from Backend.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from Backend.forms import TaskCreatorForm, TaskDetailForm, TaskFilterForm
from DBHandler.models import User, Task
from Backend.email import send_password_reset_email

link = "https://teams.microsoft.com/l/meetup-join/19%3ameeting_NmFiZjhkZTgtMTE1Yy00OGEyLTkxZjctM2EwOTljOGY5NDYy%40thread.v2/0?context=%7b%22Tid%22%3a%228bf89164-b311-40ca-a295-2e0f5f39d14e%22%2c%22Oid%22%3a%2292fe21b0-d2bb-4f46-8ad3-1b6af4cf6fc4%22%7d"

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    name = current_user.username
    tasks = User.allTask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            value.append(1)
        if form.projs.data:
            value.append(2)
        if form.travl.data:
            value.append(3)
        if form.movie.data:
            value.append(4)
        if form.birth.data:
            pass
        if form.gentk.data:
            value.append(6)    
    return render_template('index.html', title='Home', tasks=tasks, link=link, form=form)

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

@app.route('/edit_task', methods=['GET', 'POST'])
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

