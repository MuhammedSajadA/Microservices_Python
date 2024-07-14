from flask import Flask,jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run()
