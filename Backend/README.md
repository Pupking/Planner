## Description
The entire backend was done in flask. The templates are created in html with the help of jinja2.
The forms are created with the help of WTForms.
Other flask-extensions used are--> flask_sqlalchemy, flask_login, flask_migrate, flask_mail.
SMTPHandler, RotatingFileHandler are used to handle logs.

## Routes in backend
All the routes used and their functions are given below:

### Main page view routes
<p>The main filter functionality is shown here</p>
<p>route('/') and route('/index') --> route for the main page. Has the task filter and shows all tasks.
route('/index/online_meetings') --> extension of /index route but with the filter of Online meetings filter applied</p>
<p>route('/index/projects') --> extension of /index route but with the Project/Assignment deadlines filter applied</p>
<p>route('/index/travels') --> extension of /index route but with the Travel/Journey filter applied</p>
<p>route('/index/movies') --> extension of /index route but with the Movies filter applied</p>
<p>route('/index/birthday') --> extension of /index route but with the Birthday filter applied</p>
<p>route('/index/others') --> extension of /index route but with the Others filter applied filter applied</p>

### Authentication routes
<p>route('/login') --> used for login</p>
<p>route('/register') --> used to register new user</p>
<p>route('/logout') --> used to logout</p>
<p>route('/reset_password_request') --> used to request for reset password</p>
<p>route('/reset_password/<token>') --> used to reset password. This link is sent to user mail</p>

### Create routes
<p>route('/create_task') --> used to create tasks</p>
<p>route('/edit_task/<task_id>') --> used to add details to tasks based on their types. This is just used to redirect to the correct input page</p>
<p>route('/edit_task/<task_type>/<task_id>') --> used to add details to tasks of various types with help of their id.</p>
<p>Here <task_id> is used for identifying the exact task for which we want to add details.</p>
<p>Here <task_type> is a static value in the list:</p>
<ul>
    <li>onlme = Online Meetings</li>
    <li>birth = Birthday</li>
    <li>projs = Project/Assignment Deadlines</li>
    <li>travel = Travel/Journey</li>
    <li>gentk = Others</li>
    <li>movie = Movies</li>
</ul>

### Delete routes
<p>route('/delete_task/<task_id>') --> used to delete tasks based on their types. This is just used to redirect to the correct delete route.</p>
<p>route('/edit_task/<task_type>/<task_id>') --> used to delete tasks of various types with help of their id.</p>
<p>Here <task_id> is used to identify exactly which task to delete</p>
<p>Here <task_type> is a static value in the list:</p>
<ul>
    <li>onlme = Online Meetings</li>
    <li>birth = Birthday</li>
    <li>projs = Project/Assignment Deadlines</li>
    <li>travl = Travel/Journey</li>
    <li>gentk = Others</li>
    <li>movie = Movies</li>
</ul>

### Other routes
<p>route('fullview/<task_id>') --> used to view all the details of the task with help of their ids.</p>
<p>route('calendar') --> used to view the calendar.</p>

## Error Handlers
2 errors are handled in production mode:
<ol>
    <li>error 404</li>
    <li>error 500</li>
</ol>

## Forms

### Forms used for authentication features
<ol>
<li>LoginForm</li>
<li>RegistrationForm</li>
<li>ResetPasswordRequestForm</li>
<li>ResetPasswordForm<li>
</ol>
### Forms used for creating tasks and adding details to them 
<ol>
<li>TaskCreatorForm</li>
<li>TravelForm</li>
<li>TaskFilterForm</li>
<li>Onl_Birthday_Form</li>
<li>Deadline_Gen_Form</li>
<li>MovieForm</li>
</ol>

## Email
Used to send emails with the help of flask_mail.

## Templates
### Error handling templates
<ol>
<li>404.html</li>
<li>500.html</li>
</ol>
### Form templates(that are used to create tasks)
<ol>
<li>Birthday.html</li>
<li>calendar.html</li>
<li>create_task.html</li>
<li>deadline.html</li>
<li>travel.html</li>
<li>movie.html</li>
<li>general.html</li>
<li>online_meet.html</li>
</ol>
### Form templates that help in authentication
<ol>
<li>login.html</li>
<li>register.html</li>
<li>reset_password.html</li>
<li>reset_password_request.html</li>
</ol>
### Main view templates
<ol>
<li>base.html</li>
<li>index.html</li>
<li>fullview.html</li>
<li>_task.html --> Subtemplate used for ease in editing</li>
</ol>
### Email Template (used when an email is sent)
email</br>
|__reset_password.html</br>
|__reset_password.txt</br>

## Other Details
<p>The logs are stored in the directory logs which is present in the parent directory.</p>
<p>The config.py is also stored in the parent directory.</p>
<p>The db and models.py are stored in the DBHandler directory present in the parent directory.</p>
