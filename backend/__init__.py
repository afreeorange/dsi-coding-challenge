#!/usr/bin/env python
"""
Initialization file for flask app
"""
from flask import Flask
import os

__author__ = "Shalyn Guthery"
dire = os.path.abspath('templates')
app = Flask(__name__, instance_relative_config=True, template_folder=dire)
import backend.views  # load views

# Load config file
app.config.from_object('backend.config')
