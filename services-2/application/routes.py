from flask import Flask, render_template, request, Response
import random
from application import app

@app.route('/nationality', methods=['GET'])
def nationality():
    nationality = ["British", "German", "French", "Indian", "Russian", "American", "CHINESE", "JAPANESE"]
    return Response(str(random.choice(nationality)), mimetype='text/plain')