#!/usr/bin/env python
"""
Tests for database connections and actions
"""
import json
from backend.tests.base import BaseTestCase
from backend.query_database import query_database


class TestCitiesService(BaseTestCase):
    """Tests for the Cities Services."""
    def test_cities(self):
        """test passes if route is behaving correctly"""
        response = self.client.get('/cities')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('good!', data['message'])
        self.assertIn('success', data['status'])

    def test_get_city(self):
        """Test passes if correct city is returned"""
        good_city = 'Des Moines'
        result = query_database(good_city)
        self.assertIsNotNone(result)
