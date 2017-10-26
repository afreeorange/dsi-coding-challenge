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
    :param city: city to look up in database
    :return: results of query
    """
    conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                            " password=" + os.environ.get('PASSWORD'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities where name=%s LIMIT 25;", (city,))

    names = ('city_id', 'name', 'ascii_name', 'alt_name', 'state', 'lat', 'lon',
             'country', 'population', 'tz')
    results = []
    for record in cur.fetchall():
        results.append(dict(zip(names, record)))
    return results


def fuzzy_query(city):
    """
    Perform a fuzzy search on table
    :param city: city to look up in database
    :return: results of query
    """
    conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                            " password=" + os.environ.get('PASSWORD'))
    cur = conn.cursor()
    cur.execute("SELECT * FROM cities where soundex(name) = soundex(%s) OR "
                "name LIKE %s LIMIT 25;", (city, '%'+city+'%'))

    names = ('city_id', 'name', 'ascii_name', 'alt_name', 'state', 'lat', 'lon',
             'country', 'population', 'tz')
    results = []
    for record in cur.fetchall():
        results.append(dict(zip(names, record)))
    return results


def main():
    city = "Des Moines"
    result1 = query_database(city)
    print(result1)
    result2 = fuzzy_query(city)
    print(result2)


if __name__ == "__main__":
    main()
