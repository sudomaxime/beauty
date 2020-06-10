import os

mongo_initdb_database_admin = os.environ.get('MONGO_INITDB_DATABASE_ADMIN')
mongo_initdb_database_pw = os.environ.get('MONGO_INITDB_DATABASE_PASSWORD')
mongo_initdb_database_name = os.environ.get('MONGO_INITDB_DATABASE')
mongo_testing_database_name = 'tests' 

class Production():
    DEBUG = False
    MONGO_URI = f'mongodb://{mongo_initdb_database_admin}:{mongo_initdb_database_pw}@mongo:27017/{mongo_initdb_database_name}'

class Development():
    DEBUG = True
    MONGO_URI = f'mongodb://{mongo_initdb_database_admin}:{mongo_initdb_database_pw}@mongo:27017/{mongo_initdb_database_name}'

class Testing():
    DEBUG = True
    TESTING = True
    MONGO_URI = f'mongodb://{mongo_initdb_database_admin}:{mongo_initdb_database_pw}@mongo:27017/{mongo_testing_database_name}'

env = dict(
    production=Production,
    development=Development,
    testing=Testing
)