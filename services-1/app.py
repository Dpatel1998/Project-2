from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
import requests
import os
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")

db = SQLAlchemy(app)

class Soldier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(30), nullable=False)
    player_class = db.Column(db.String(30), nullable=False)
    build = db.Column(db.String(500), nullable=False)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def gen():
    nationality_response = requests.get("http://soldier-gen_service2:5000/nationality").text
    player_class_response = requests.get("http://soldier-gen_service3:5000/player_class").text
    build_response = requests.post("http://soldier-gen_service4:5000/build", data = player_class_response.text).text
    
    new_build = Soldier(nationality = nationality_response, player_class = player_class_response, build = build_response)
    db.session.add(new_build)
    db.session.commit()

    return render_template('index.html', nationality_response=nationality_response, player_class_response=player_class_response, build_response=build_response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port= 5000)
