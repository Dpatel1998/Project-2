from flask import Flask, render_template, request, Response
from application import app

@app.route('/build', methods=['POST','GET'])
def build():
    player_class = request.data.decode('utf-8')

    if player_class == "Machine-Gunner":
        build = 'A soldier who carries an auto-firing, autoloading firearm designed for sustained direct fire with fully powered cartridges.'
    elif player_class == "Sniper":
        build = 'Marksman who engages targets from positions of concealment or at distances exceeding the targets detection capabilities.'
    elif player_class == "Medic":
        build = 'Combat Medic Specialist is responsible for providing emergency medical treatment at a point of wounding in a combat environment.'
    elif player_class == "Spy":
        build = 'A person employed by the army to secretly obtain information on an enemy.'
    elif player_class == "Engineer":
        build = 'The Engineers are combat soldiers with a technical edge.'
    elif player_class == "Translator":
        build = 'The Translator is responsible for conducting interpretation and preparing translations between foreign languages.'
    elif player_class == "Tankman":
        build = 'Specialist soldier trained to handle Tanks.'
    elif player_class == "General":
        build = 'A general officer is an officer of high rank.'
    elif player_class == "INFANTRY-SOLDIER":
        build = 'A infeantry soldier is on the front line on peace-keeping missions and some of the most active type of soldier.'
    
    
    else:
        build = "Soldier not compatible"

    return Response(build, mimetype='text/plain')