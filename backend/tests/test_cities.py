#!/usr/bin/env python
"""
Tests for database connections and actions
"""
import json
from backend.tests.base import BaseTestCase


class TestCitiesService(BaseTestCase):
    """Tests for the Cities Services."""
    def test_cities(self):
        """test passes if route is behaving correctly"""
        response = self.client.get('/cities')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('good!', data['message'])
        self.assertIn('success', data['status'])
