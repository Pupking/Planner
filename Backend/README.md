## Description
The entire backend was done in flask. The templates are created in html with the help of jinja2.
The forms are created with the help of WTForms.
Other flask-extensions used are--> flask_sqlalchemy, flask_login, flask_migrate, flask_mail.
SMTPHandler, RotatingFileHandler are used to handle logs.

## Routes in backend
All the routes used and their functions are given below:

### Main page view routes
The main filter functionality is shown here
route('/') and route('/index') --> route for the main page. Has the task filter and shows all tasks.
route('/index/online_meetings') --> extension of /index route but with the filter of Online meetings filter applied
route('/index/projects') --> extension of /index route but with the Project/Assignment deadlines filter applied
route('/index/travels') --> extension of /index route but with the Travel/Journey filter applied
route('/index/movies') --> extension of /index route but with the Movies filter applied
route('/index/birthday') --> extension of /index route but with the Birthday filter applied
route('/index/others') --> extension of /index route but with the Others filter applied filter applied

### Authentication routes
route('/login') --> used for login
route('/register') --> used to register new user
route('/logout') --> used to logout
route('/reset_password_request') --> used to request for reset password 
route('/reset_password/<token>') --> used to reset password. This link is sent to user mail

### Create routes
route('/create_task') --> used to create tasks
route('/edit_task/<task_id>') --> used to add details to tasks based on their types. This is just used to redirect to the correct input page
route('/edit_task/<task_type>/<task_id>') --> used to add details to tasks of various types with help of their id.
Here <task_id> is used for identifying the exact task for which we want to add details.
Here <task_type> is a static value in the list:
<ul>
    <li>onlme = Online Meetings</li>
    <li>birth = Birthday</li>
    <li>projs = Project/Assignment Deadlines</li>
    <li>travel = Travel/Journey</li>
    <li>gentk = Others</li>
    <li>movie = Movies</li>
</ul>

### Delete routes
route('/delete_task/<task_id>') --> used to delete tasks based on their types. This is just used to redirect to the correct delete route.
route('/edit_task/<task_type>/<task_id>') --> used to delete tasks of various types with help of their id.
Here <task_id> is used to identify exactly which task to delete
Here <task_type> is a static value in the list:
<ul>
    <li>onlme = Online Meetings</li>
    <li>birth = Birthday</li>
    <li>projs = Project/Assignment Deadlines</li>
    <li>travl = Travel/Journey</li>
    <li>gentk = Others</li>
    <li>movie = Movies</li>
</ul>

### Other routes
route('fullview/<task_id>') --> used to view all the details of the task with help of their ids.
route('calendar') --> used to view the calendar.

## Error Handlers
2 errors are handled in production mode:
<ol>
    <li>error 404</li>
    <li>error 500</li>
</ol>

## Forms
### Forms used for authentication features
LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
### Forms used for creating tasks and adding details to them 
TaskCreatorForm, TravelForm, TaskFilterForm, Onl_Birthday_Form, Deadline_Gen_Form, MovieForm

## Email
Used to send emails with the help of flask_mail.

## Templates
### Error handling templates
404.html
500.html

### Form templates(that are used to create tasks)
Birthday.html
calendar.html
create_task.html
deadline.html
travel.html
movie.html
general.html
online_meet.html

### Form templates that help in authentication
login.html
register.html
reset_password.html
reset_password_request.html

### Main view templates
base.html
index.html
fullview.html
_task.html --> Subtemplate used for ease in editing

### Email Template (used when an email is sent)
email
|__reset_password.html
|__reset_password.txt

## Other Details
The logs are stored in the directory logs which is present in the parent directory.
The config.py is also stored in the parent directory.
The db and models.py are stored in the DBHandler directory present in the parent directory.
