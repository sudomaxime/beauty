import os
import unittest
from app import create_app
from app.settings import env
from flask_script import Manager

mode = os.environ.get('MODE') or 'development'
app = create_app(env[mode])
manager = Manager(app)

@manager.command
def run():
    """Starts the app."""
    app.run(host='0.0.0.0')

@manager.command
def test():
    """Runs the unit and integration tests."""
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()