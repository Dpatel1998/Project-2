from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_player_class(self):
        with patch("random.choice") as r:
            r.return_value = "Medic"
            response = self.client.get(url_for('nationality'))
            self.assertEqual(b'Medic', response.data)