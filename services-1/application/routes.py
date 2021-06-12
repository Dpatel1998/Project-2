from flask import Flask, render_template, request, jsonify
from sqlalchemy import desc
import requests
from application.models import Soldier
from application import app, db

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def gen():
    nationality_response = requests.get("http://services-2:5000/nationality").text
    player_class_response = requests.get("http://services-3:5000/player_class").text
    build_response = requests.post("http://services-4:5000/build", data = player_class_response).text
    

    new_build = Soldier(nationality = nationality_response, player_class = player_class_response, build = build_response)
    db.session.add(new_build)
    db.session.commit()

    view_Soldier = Soldier.query.order_by(desc(Soldier.id)).all()

    return render_template('index.html', nationality_response=nationality_response, player_class_response=player_class_response, build_response=build_response,view_players=view_Soldier)


