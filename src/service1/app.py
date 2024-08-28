import socket
import requests
from flask import Flask, jsonify, render_template


app = Flask(__name__)

MICROSERVICE_2 = 'http://microservice2:5001'

def user_os_details():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return hostname, hostip


@app.route("/")
def index():
    return "<p> welcome to MicroService !"


@app.route("/health")
def health():
    return jsonify(status="MicroService 1 is running ...")

@app.route('/users')
def get_users():
    response = requests.get(f'{MICROSERVICE_2}/get-gh-users')
    return render_template('index.html', users=response.json())


@app.route("/os-details")
def details():
    host_name, host_ip = user_os_details()
    return jsonify(hostname=host_name, hostip=host_ip)

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
