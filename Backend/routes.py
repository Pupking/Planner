from datetime import datetime, timezone
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from Backend import app, db
from Backend.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from Backend.forms import TaskCreatorForm, TravelForm, TaskFilterForm, Onl_Birthday_Form, Deadline_Gen_Form, MovieForm
from DBHandler.models import User, Task, Online_meetings, Deadlines, Travel, Birthday, General, Movie
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
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
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
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
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
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route('/index/travels', methods=['GET', 'POST'])
@login_required
def travels():
    tasks = User.projectstask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
        if form.birth.data:
            return redirect(url_for('birthday'))
        if form.gentk.data:
            return redirect(url_for('others'))
        if form.index.data:
            return redirect(url_for('index'))
    return render_template('index.html', title='Home', tasks=tasks, form=form)

@app.route('/index/movies', methods=['GET', 'POST'])
@login_required
def movies():
    tasks = User.movietask(current_user)
    form = TaskFilterForm()
    if form.validate_on_submit():
        if form.onlme.data:
            return redirect(url_for('online_meetings'))
        if form.projs.data:
            return redirect(url_for('projects'))
        if form.travl.data:
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
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
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
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
            return redirect(url_for('travels'))
        if form.movie.data:
            return redirect(url_for('movies'))
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
        combine = datetime.combine(form.date.data, form.time.data)
        task = Task(creator=current_user, title=form.title.data, task_type=form.task_type.data, timestamp=combine)
        db.session.add(task)
        db.session.commit()
        flash('Task successfully created!! Add few more details')
        return redirect(url_for('edit_task',task_id=task.id))
    if request.method == 'GET':
        form.date.data = datetime.now()
        form.time.data = datetime.now()
    return render_template('create_task.html', title='Create Task', form=form)

@app.route('/edit_task/<task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_type = task.task_type
    if task_type == 'onlme':
        return redirect(url_for('onlme',task_id=task.id))
    if task_type == 'birth':
        return redirect(url_for('birth',task_id=task.id))
    if task_type == 'projs':
        return redirect(url_for('projs',task_id=task.id))
    if task_type == 'gentk':
        return redirect(url_for('gentk',task_id=task.id))
    if task_type == 'travl':
        return redirect(url_for('travel',task_id=task.id))
    if task_type == 'movie':
        return redirect(url_for('movie',task_id=task.id))
    
@app.route('/edit_task/onlme/<task_id>', methods=['GET', 'POST'])
@login_required
def onlme(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_title = task.title
    form = Onl_Birthday_Form()
    if form.validate_on_submit():
        t = Online_meetings(parent1=task, link=form.link.data, desc=form.desc.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('online_meet.html', title='Add Details', form=form, task_title=task_title)

@app.route('/edit_task/birth/<task_id>', methods=['GET', 'POST'])
@login_required
def birth(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_title = task.title
    form = Onl_Birthday_Form()
    if form.validate_on_submit():
        t = Birthday(parent4=task, location=form.link.data, name=form.desc.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('Birthday.html', title='Add Details', form=form, task_title=task_title)

@app.route('/edit_task/projs/<task_id>', methods=['GET', 'POST'])
@login_required
def projs(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_title = task.title
    form = Deadline_Gen_Form()
    if form.validate_on_submit():
        combine = datetime.combine(form.start_date.data, form.start_time.data)
        t = Deadlines(parent2=task, date=combine, desc=form.desc.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('deadline.html', title='Add Details', form=form, task_title=task_title)

@app.route('/edit_task/gentk/<task_id>', methods=['GET', 'POST'])
@login_required
def gentk(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_title = task.title
    form = Deadline_Gen_Form()
    if form.validate_on_submit():
        combine = datetime.combine(form.start_date.data, form.start_time.data)
        t = General(parent5=task, time=combine, desc=form.desc.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('general.html', title='Add Details', form=form, task_title=task_title)

@app.route('/edit_task/travel/<task_id>', methods=['GET', 'POST'])
@login_required
def travel(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_title = task.title
    form = TravelForm()
    if form.validate_on_submit():
        combine1 = datetime.combine(form.start_date.data, form.start_time.data)
        combine2 = datetime.combine(form.finish_date.data, form.finish_time.data)
        t = Travel(parent3=task, start_date=combine1, end_date=combine2, source=form.source.data, destination=form.destination.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    if request.method == 'GET':
        form.start_date.data = task.timestamp
        form.start_time.data = task.timestamp
        form.finish_date.data = datetime.now()
        form.finish_time.data = datetime.now()
    return render_template('task_detail.html', title='Add Details', form=form, task_title=task_title)

@app.route('/edit_task/movie/<task_id>', methods=['GET', 'POST'])
@login_required
def movie(task_id):
    task = Task.query.filter_by(id = task_id).first()
    task_title = task.title
    form = MovieForm()
    if form.validate_on_submit():
        t = Movie(parent6=task, name=form.name.data, desc=form.desc.data, location=form.loc.data)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('movie.html', title='Add Details', form=form, task_title=task_title)

@app.route('/delete_task/<title>', methods=['GET','POST'])
@login_required
def delete_task(title):
    task = Task.query.filter_by(title=title).first()
    task_type = task.task_type
    task_id = task.id
    if task_type == 'onlme':
        t = Online_meetings.query.filter_by(id=task_id).first()
        db.session.delete(t)
        db.session.delete(task)
        db.session.commit()
    if task_type == 'projs':
        t = Deadlines.query.filter_by(id=task_id).first()
        db.session.delete(t)
        db.session.delete(task)
        db.session.commit()
    if task_type == 'travl':
        t = Travel.query.filter_by(id=task_id).first()
        db.session.delete(t)
        db.session.delete(task)
        db.session.commit()
    if task_type == 'birth':
        t = Birthday.query.filter_by(id=task_id).first()
        db.session.delete(t)
        db.session.delete(task)
        db.session.commit()
    if task_type == 'gentk':
        t = General.query.filter_by(id=task_id).first()
        db.session.delete(t)
        db.session.delete(task)
        db.session.commit()
    if task_type == 'movie':
        t = Movie.query.filter_by(id=task_id).first()
        db.session.delete(t)
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/fullview/<task_id>')
@login_required
def fullview(task_id):
    task = Task.query.filter_by(id=task_id).first()
    task_type = task.task_type
    task_id = task.id
    if task_type == 'onlme':
        print(task_id)
        t1 = Online_meetings.query.filter_by(taskid=task_id).first()
        return render_template('fullview.html', task=task, t1=t1)
    if task_type == 'projs':
        t2 = Deadlines.query.filter_by(taskid=task_id).first()
        return render_template('fullview.html', task=task, t2=t2)
    if task_type == 'travl':
        t3 = Travel.query.filter_by(taskid=task_id).first()
        return render_template('fullview.html', task=task, t3=t3)
    if task_type == 'birth':
        t4 = Birthday.query.filter_by(taskid=task_id).first()
        return render_template('fullview.html', task=task, t4=t4)
    if task_type == 'gentk':
        t5 = General.query.filter_by(taskid=task_id).first()
        return render_template('fullview.html', task=task, t5=t5)
    if task_type == 'movie':
        t6 = Movie.query.filter_by(taskid=task_id).first()
        return render_template('fullview.html', task=task, t6=t6)
