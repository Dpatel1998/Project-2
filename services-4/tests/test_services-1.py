from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestBuild(TestBase):
    def test_gunner(self):
        response = self.client.post(url_for('build'), data = "Machine-Gunner",)
        self.assertIn(b'A soldier who carries an auto-firing, autoloading firearm designed for sustained direct fire with fully powered cartridges.', response.data)
    
    def test_Sniper(self):
        response = self.client.post(url_for('build'), data = "Sniper",)
        self.assertIn(b'Marksman who engages targets from positions of concealment or at distances exceeding the targets detection capabilities.', response.data)
    
    def test_medic(self):
        response = self.client.post(url_for('build'), data = "Medic",)
        self.assertIn(b'Combat Medic Specialist is responsible for providing emergency medical treatment at a point of wounding in a combat environment.', response.data)
    
    def test_spy(self):
        response = self.client.post(url_for('build'), data = "Spy",)
        self.assertIn(b'A person employed by the army to secretly obtain information on an enemy.', response.data)
    
    def test_engineer(self):
        response = self.client.post(url_for('build'), data = "Engineer",)
        self.assertIn(b'The Engineers are combat soldiers with a technical edge.', response.data)
    
    def test_translator(self):
        response = self.client.post(url_for('build'), data = "Translator",)
        self.assertIn(b'The Translator is responsible for conducting interpretation and preparing translations between foreign languages.', response.data)
    
    def test_tankman(self):
        response = self.client.post(url_for('build'), data = "Tankman",)
        self.assertIn(b'Specialist soldier trained to handel Tanks.', response.data)
    
    def test_general(self):
        response = self.client.post(url_for('build'), data = "General",)
        self.assertIn(b'A general officer is an officer of high rank.', response.data)
    
    def test_else(self):
        response = self.client.post(url_for('build'), data = "Soldier not compatible",)
        self.assertNotIn(b'Marksman who engages targets from positions of concealment or at distances exceeding the targets detection capabilities.', response.data)