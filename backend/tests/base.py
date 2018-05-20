#!/usr/bin/env python
"""
Base testcase
"""
from backend import app
from flask_testing import TestCase


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('backend.config')
        return app
