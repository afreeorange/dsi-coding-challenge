#!/usr/bin/env python
"""
Query PostgreSQL database table and receive
JSON object as result
"""
import psycopg2
import os
import json

__author__ = "Shalyn Guthery"


def query_database(city):
    """
    :return: JSON object
    """
    conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                            " password=" + os.environ.get('PASSWORD'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities where ascii_name=%s LIMIT 25;", (city,))

    names = ('city_id', 'name', 'ascii_name', 'alt_name', 'state', 'lat', 'lon',
             'country', 'population', 'tz')
    results = []
    for record in cur.fetchall():
        results.append(dict(zip(names, record)))
    return results


def main():
    city = "Des Moines"
    result = query_database(city)
    print(result)


if __name__ == "__main__":
    main()
