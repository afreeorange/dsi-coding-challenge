#!/usr/bin/env python
"""
View configuration file
"""
from flask import render_template, jsonify
from backend import app
from backend.query_database import query_database

__author__ = "Shalyn Guthery"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cities/<string:city>', methods=['GET'])
def cities(city):
    print(city)
    result = query_database(city)
    response_object = {
        'status': 'success',
        'data': result
    }
    return jsonify(response_object), 200
