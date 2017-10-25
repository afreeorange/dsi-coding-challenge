#!/usr/bin/env python
"""
View configuration file
"""
from flask import render_template
from app import app

__author__ = "Shalyn Guthery"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cities')
def cities():
    return render_template("cities.html")
