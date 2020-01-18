import requests
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, send_from_directory, render_template, Blueprint
from config import config 
import base64, json

app = Flask(__name__)

cors = CORS(app, resources=r'/*')

@app.route('/register', methods=['POST'])
def register():
    try:
        gst_in = request.form['gstin']
        pan = request.files['pan']
        adhaar = request.files['adhaar']
        password = request.files['password']
        respan = requests.post(config['visionApi'], json = {"method": "base64", "Bro4uKey":"s#h@#kf@t!&*@#k735t!@t!@47xbe@#!@^#Hg", "fdata": str(base64.b64encode(pan.read()))[2:-1]}).json()
        resadhaar = requests.post(config['visionApi'], json = {"method": "base64", "Bro4uKey":"s#h@#kf@t!&*@#k735t!@t!@47xbe@#!@^#Hg", "fdata": str(base64.b64encode(adhaar.read()))[2:-1]}).json() 
        match_score = 0
        if type(respan['body']) == str or type(resadhaar['body']) == str:
            return jsonify({'res':[respan.json(), resadhaar.json()]}), 400
        l = len(respan['body']['name'])
        for i in len(respan['body']['name']):
            if respan['body']['name'][i] == resadhaar['body']['name'][i]:
                match_score = match_score + 1
        match_score = (match_score / l)* 100
        if match_score >= 75.0 and respan['body']['pan']==gst_in[2:-3]:
            #Insert into db. 
            #config['mongoclient'].users.insert({'name':respan['body']['name'], 'password': password,... })
            return jsonify({'res':'success'}), 200
        else:
            return jsonify({'res':'failed'}), 400
    except:
        return jsonify({'msg':'my underwear came out'}), 500

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5244, debug=True)