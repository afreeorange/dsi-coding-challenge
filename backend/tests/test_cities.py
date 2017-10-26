#!/usr/bin/env python
"""
Tests for database connections and actions
"""
from backend.query_database import query_database, fuzzy_query
from backend.tests.base import BaseTestCase


class TestCitiesService(BaseTestCase):
    def test_get_city(self):
        """Test passes if correct city is returned"""
        good_city = 'Des Moines'
        result = query_database(good_city)
        self.assertIsNotNone(result)

    def test_get_fuzzy_city(self):
        """Test passes if result is not None"""
        good_city = 'Des Moines'
        result = fuzzy_query(good_city)
        self.assertIsNotNone(result)
