from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, DateField, TimeField, DateTimeField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from DBHandler.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')


class TaskCreatorForm(FlaskForm):
    title = StringField('Enter Task', validators=[DataRequired()])
    task_type = SelectField(
        'Select Task Type',
        choices=[('onlme','Online Meeting'), ('projs','Project/Assignment Deadlines'), ('travl','Travel/Journey'), ('movie','Movie'), ('birth','Birthdays/Anniversaries'), ('gentk','Others')], validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d')
    time = TimeField('Time', format='%H:%M')
    submit = SubmitField('Next >')

class TravelForm(FlaskForm):
    start_date = DateField('Date', format='%Y-%m-%d')
    start_time = TimeField('Time', format='%H:%M')
    finish_date = DateField('Date', format='%Y-%m-%d')
    finish_time = TimeField('Time', format='%H:%M')
    source = StringField('Source')
    destination = StringField('Destination')
    submit = SubmitField('Finish')

class Onl_Birthday_Form(FlaskForm):
    link = StringField('Meeting Link', validators=[DataRequired()])
    desc = TextAreaField('Enter Description', validators=[Length(min=0, max=350)])
    submit = SubmitField('Finish')

class Deadline_Gen_Form(FlaskForm):
    start_date = DateField('Date', format='%Y-%m-%d')
    desc = TextAreaField('Enter Description', validators=[Length(min=0, max=350)])
    submit = SubmitField('Finish')

class MovieForm(FlaskForm):
    name = StringField('Movie Name', validators=[DataRequired()])
    loc = StringField('Enter Location Link',validators=[DataRequired()])
    desc = TextAreaField('Enter Description', validators=[Length(min=0, max=150)])
    submit = SubmitField('Finish')

class TaskFilterForm(FlaskForm):
    onlme = SubmitField('Online Meetings')
    projs = SubmitField('Projects/Assignments')
    travl = SubmitField('Travel/Journey')
    movie = SubmitField('Movie/Concert Reservations')
    birth = SubmitField('Birthdays')
    gentk = SubmitField('Others')
    index = SubmitField('Show all tasks')
