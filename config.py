import os 
basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
    SERVER_NAME = os.environ.get('SERVER_NAME') or 'localhost.dev:5000'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nunca-lo-adivinaras'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL=True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS =  os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['your-email@example.com']
    BOOTSTRAP_SERVE_LOCAL = True