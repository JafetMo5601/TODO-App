import os


SECRET_KEY = os.environ.get('TODO-App_Secret-Key')
DBPASSWD = os.environ.get('DBPASSWD')
SQLALCHEMY_DATABASE_URI = 'mysql://root:{0}@localhost/todo'.format(DBPASSWD)