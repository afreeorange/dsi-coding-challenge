#!/usr/bin/env python
"""
Initialization file for flask app
"""
from flask import Flask

__author__ = "Shalyn Guthery"

app = Flask(__name__, instance_relative_config=True)
import views  # load views

# Load config file
app.config.from_object('backend.config')
