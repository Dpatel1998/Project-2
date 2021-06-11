from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
import requests
from application.models import Soldier 
from application import app, db

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def gen():
    nationality_response = requests.get("http://soldier-gen_service2:5000/race")
    player_class_response = requests.get("http://soldier-gen_service3:5000/player_class")
    build_response = requests.post("http://soldier-gen_service4:5000/build", data = player_class_response.text)
    
    new_build = Soldier(nationality = nationality_response.text, player_class = player_class_response.text, build = build_response.text)
    db.session.add(new_build)
    db.session.commit()

    return render_template('index.html', race=nationality_response.text, player_class=player_class_response.text, build=build_response.text)
