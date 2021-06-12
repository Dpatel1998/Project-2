from flask import url_for
from flask_testing import TestCase
import requests_mock 
import requests
from application import app, db
from application.models import Soldier

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app
    
    def setUp(self):
        db.create_all()
        db.session.add(Soldier(nationality = "Russian", player_class = "Spy", build = "A person employed by the army to secretly obtain information on an enemy."))
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestGenerator(TestBase):
    def test_gen(self):
        response = self.client.get(url_for('gen'))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def test_index(self):
        with requests_mock.mock() as g:
            g.get("http://services-2:5000/nationality", text = "Russian")
            g.get("http://services-3:5000/player_class", text = "Spy")
            g.post("http://services-4:5000/build", text = "A person employed by the army to secretly obtain information on an enemy.")
            
            response = self.client.get(url_for('gen'))
        self.assertNotIn("British", response.data.decode())
        self.assertIn("Spy", response.data.decode())
        self.assertIn("A person employed by the army to secretly obtain information on an enemy.", response.data.decode())
