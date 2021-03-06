import os
basedir = os.path.abspath(os.path.dirname(__file__))
dbdir = os.path.join(basedir, 'DBHandler')
username='root'
password='Trial#123'
host='localhost'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Trial-Key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(dbdir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'localhost'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 8025)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['dsh17082001@gmail.com']
