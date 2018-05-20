#!/usr/bin/env python
"""
View configuration file for route information
"""
from backend import app
from backend.query_database import query_database, fuzzy_query
from flask import render_template, jsonify, request

__author__ = "Shalyn Guthery"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cities/<city>', methods=['GET'])
def cities(city):
    result = query_database(city.upper())
    if result != []:
        response_object = {
            'status': 'success',
            'cities': result
        }
        return jsonify(response_object), 200
    else:
        response_object = {
            'status': 'name error',
            'message': 'city could not be found'
        }
        return jsonify(response_object), 400


@app.route('/cities', methods=['GET'])
def cities_like():
    cid = request.args.get('like')
    if cid is not None:
        result = fuzzy_query(cid.upper())
        if result != []:
            response_object = {
                'status': 'success',
                'cities': result
            }
            return jsonify(response_object), 200
        else:
            response_object = {
                'status': 'name error',
                'message': 'city could not be found'
            }
            return jsonify(response_object), 400

    return render_template("cities.html")

