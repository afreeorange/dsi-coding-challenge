#!/usr/bin/env python
"""
Manage app
"""
import unittest

from backend import app
from flask_script import Manager

manager = Manager(app)


@manager.command
def test():
    """Run unit tests"""
    tests = unittest.TestLoader().discover('backend/tests', pattern='test*.py')
    result = unittest.TextTestRunner().run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == '__main__':
    manager.run()
