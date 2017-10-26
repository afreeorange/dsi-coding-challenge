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
from queries import create_query, check_query

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
    # convert alt names list to uppercase
    altnames = [x.upper() for x in altnames]
    stmt = "INSERT INTO cities (city_id, name, ascii_name, alt_name, state, " \
           "lat, lon, country, population, tz) VALUES (%s, %s, %s, %s, %s, " \
           "%s, %s, %s, %s, %s);""", (int(fields[0]), fields[1].upper(),
                                      fields[2].upper(), altnames,
                                      fields[10].upper(), float(fields[4]),
                                      float(fields[5]), fields[8].upper(),
                                      int(fields[14]), fields[17].upper())
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


def check_for_table():
    """
    Check to see if our table currently exists
    :return: exist_bool (BOOLEAN) true if table exists
    """
    conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                            " password=" + os.environ.get('PASSWORD'))
    cur = conn.cursor()
    cur.execute(check_query)
    exist_bool = bool(cur.fetchone()[0])
    cur.close()
    conn.commit()

    return exist_bool


def execute_query(query):
    """
    :param query: string to use with psycopg2
    :return: None
    """
    conn = psycopg2.connect("dbname=" + os.environ.get('DB') +
                            " password=" + os.environ.get('PASSWORD'))
    cur = conn.cursor()
    cur.execute(query)
    cur.close()
    conn.commit()


def main():
    basepath = os.getcwd()
    path = basepath + '/data/canada_usa_cities.tsv'

    table_exists = check_for_table()
    if table_exists:
        # drop table
        execute_query("DROP TABLE cities;")
    else:
        # create new table
        create_table()

    # Load data from path into table created by create_table()
    load_data(path)


if __name__ == '__main__':
    main()
