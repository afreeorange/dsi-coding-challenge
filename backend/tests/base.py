#!/usr/bin/env python
"""
Base testcase
"""
from flask_testing import TestCase
from backend import app


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('backend.config')
        return app
