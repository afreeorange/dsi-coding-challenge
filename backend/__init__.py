#!/usr/bin/env python
"""
Initialization file for flask app
"""
from flask import Flask, jsonify

__author__ = "Shalyn Guthery"

app = Flask(__name__, instance_relative_config=True)
#from app import views  # load views

# Load config file
app.config.from_object('backend.config')


# route info
@app.route('/cities', methods=['GET'])
def cities():
    return jsonify({
        'status': 'success',
        'message': 'good!'
    })

