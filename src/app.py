from flask import Flask,jsonify, render_template
import socket

app = Flask(__name__)

@app.route('/ip')
def Ip():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)
    return str(hostname) ,str(host_ip)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/Test')
def test():
    return 'test'

@app.route('/check')
def Check():
    return jsonify(
        status="UP"
    )

@app.route('/details')
def Details():
    hostname,ip = Ip()
    return render_template('index.html',HOSTNAME=hostname,IP=ip)

if __name__ == '__main__':
    app.run()
