from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from hashlib import md5
from Backend import db, app, login
from time import time
import jwt

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    tasks = db.relationship('Task', backref='creator', lazy='dynamic')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def avatar(self,size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest,size)
      
    def allTask(self):
        own = Task.query.filter_by(user_id = self.id).order_by(Task.timestamp.desc())
        return own
      
    def birthdaytask(self):
        own = Task.query.filter_by(task_type = 'birth').order_by(Task.timestamp.desc())
        return own
      
    def movietask(self):
        own = Task.query.filter_by(task_type = 'movie').order_by(Task.timestamp.desc()) 
        return own
      
    def traveltask(self):
        own = Task.query.filter_by(task_type = 'travl').order_by(Task.timestamp.desc()) 
        return own
      
    def projectstask(self):
        own = Task.query.filter_by(task_type = 'projs').order_by(Task.timestamp.desc()) 
        return own
      
    def onlinemeetingstask(self):
        own = Task.query.filter_by(task_type = 'onlme').order_by(Task.timestamp.desc()) 
        return own
      
    def othertask(self):
        own = Task.query.filter_by(task_type = 'gentk').order_by(Task.timestamp.desc()) 
        return own 
   

    def allTask(self):
        own = Task.query.filter_by(user_id = self.id)
        return own
    

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                            algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    def __repr__(self):
        return '<User {}>'.format(self.username)
      
    def adduser(self, expires_in=600):
            return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task_type = db.Column(db.String(5))
    online = db.relationship('Online_meetings',backref = 'parent1',lazy = 'dynamic')
    deadline = db.relationship('Deadlines',backref = 'parent2',lazy = 'dynamic')
    travel = db.relationship('Travel',backref = 'parent3',lazy = 'dynamic')
    birthday = db.relationship('Birthday',backref = 'parent4',lazy = 'dynamic')
    general = db.relationship('General',backref = 'parent5',lazy = 'dynamic')
    movie = db.relationship('Movie',backref = 'parent6',lazy = 'dynamic')
    def onlinetask(self,user):
        own = Task.query.join(
            Online_meetings,(id == Online_meetings.taskid).filter(user_id = user.id)
        )
        return own
    def deadlinetask(self,user):
        own = Task.query.join(
            Deadlines,(id == Deadlines.taskid).filter(user_id = user.id)
        ) 
        return own
    def traveltask(self,user):
        own = Task.query.join(
            Travel,(id == Travel.taskid).filter(user_id = user.id)
        ) 
        return own
    def birthdaytask(self,user):
        own = Task.query.join(
         Birthday ,(id == Travel.taskid).filter(user_id = user.id)
        ) 
        return own
    def generaltask(self,user):
        own = Task.query.join(
         General ,(id == General.taskid).filter(user_id = user.id)
        ) 
        return own
    def movietask(self,user):
        own = Task.query.join(
         Movie ,(id == Movie.taskid).filter(user_id = user.id)
        ) 
        return own
    
    def __repr__(self):
        return '<Task {}>'.format(self.title)
      
class Online_meetings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer,db.ForeignKey('task.id'))
    link = db.Column(db.String(300))
    host = db.Column(db.String(50))
    desc = db.Column(db.String(100))

class Deadlines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer,db.ForeignKey('task.id'))
    desc = db.Column(db.String(300))

class Travel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer,db.ForeignKey('task.id'))
    source = db.Column(db.String(50))
    destination = db.Column(db.String(50))

class Birthday(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer,db.ForeignKey('task.id'))
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))

class General(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer,db.ForeignKey('task.id'))
    desc = db.Column(db.String(150))
    emoji = db.Column(db.String(10))

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer,db.ForeignKey('task.id'))
    name = db.Column(db.String(100))
    desc = db.Column(db.String(150))
    location = db.Column(db.String(150))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
