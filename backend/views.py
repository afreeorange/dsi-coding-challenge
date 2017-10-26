#!/usr/bin/env python
"""
View configuration file
"""
from flask import render_template, jsonify, request
from backend import app
from backend.query_database import query_database, fuzzy_query

__author__ = "Shalyn Guthery"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cities/<city>', methods=['GET'])
def cities(city):
    result = query_database(city)
    response_object = {
        'status': 'success',
        'cities': result
    }
    return jsonify(response_object), 200


@app.route('/cities', methods=['GET'])
def cities_like():
    cid = request.args.get('like')
    result = fuzzy_query(cid)
    response_object = {
        'status': 'success',
        'cities': result
    }
    return jsonify(response_object), 200
