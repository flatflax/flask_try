import os


# configurationb
DATABASE = 'dashboard.db'
DEBUG = True
SECRET_KEY = 'my_precious'

# grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

# REDIS_HOST = '43.82.163.74'
# REDIS_PORT = 6379
# REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False