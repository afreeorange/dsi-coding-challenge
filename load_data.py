#!/usr/bin/env python
"""
Load dataset into a new PostGreSQL table

Dataset - USA/Canada cities
Fields used include id, name, ascii_name, alt_name, lat, lon,
country, population, tz

location field consists of a point (longitude, latitude)

"""
import psycopg2
import os
from queries import create_query

__author__ = "Shalyn Guthery"


def create_table():
    """
    Establish connection to localhost
    Create table to house dataset
    :return: None
    """
    try:
        conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                                " password=" + os.environ.get('PASSWORD'))
        cur = conn.cursor()
        cur.execute(create_query)
        cur.close()
        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_insert(fields):
    """
    Create insert string for a given row in the dataset
    :param fields: list of fields, some of which to insert
    :return: insert string
    """
    altnames = fields[3].split(',')
    stmt = "INSERT INTO cities (city_id, name, ascii_name, alt_name, state, " \
           "lat, lon, country, population, tz) VALUES (%s, %s, %s, %s, %s, " \
           "%s, %s, %s, %s, %s);""", (int(fields[0]), fields[1], fields[2],
                                      altnames, fields[10], float(fields[4]),
                                      float(fields[5]), fields[8],
                                      int(fields[14]), fields[17])
    return stmt


def load_data(filename):
    """
    Load dataset into table
    :param filename: path to file containing data
    :return: None
    """
    conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                            " password=" + os.environ.get('PASSWORD'))
    cur = conn.cursor()
    with open(filename, 'r') as f:
        header = f.readline()
        for line in f:
            line = line.strip()
            temp = line.split('\t')
            insert_stmt = create_insert(temp)
            cur.execute(insert_stmt[0], insert_stmt[1])
            conn.commit()

    cur.close()
    conn.close()
    return None


def main():
    basepath = '/home/personal/github/dsi-coding-challenge/'
    path = basepath + 'data/canada_usa_cities.tsv'

    create_table()
    load_data(path)


if __name__ == '__main__':
    main()
