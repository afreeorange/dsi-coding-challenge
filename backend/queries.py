#!/usr/bin/env python
"""
Contains queries used to setup database
"""

__author__ = "Shalyn Guthery"

create_query = """ CREATE TABLE cities (
                    city_id INTEGER PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    ascii_name VARCHAR(255) NOT NULL,
                    alt_name VARCHAR(255)[],
                    state VARCHAR(5),
                    lat REAL NOT NULL,
                    lon REAL NOT NULL,
                    country VARCHAR(5),
                    population INTEGER,
                    tz VARCHAR(255))
                    """
