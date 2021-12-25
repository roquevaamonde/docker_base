from flask import Flask
from flask import request
from pytube import YouTube
import shutil
from moviepy.editor import *
import datetime
import threading
import os
import json

app = Flask(__name__)  # creamos flask instance
#incluimos para mewrga

@app.route('/health_check') 
def health_check():
    check = request.args.get('check', 'error')

    salida = {
        "titulo": str(check),
        "autor": "Roque Vaamonde para su laboratorio de pruebas"
    }

    return salida


app.run(debug=True, host='0.0.0.0', port=9000)
