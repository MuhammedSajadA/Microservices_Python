from flask import Flask,jsonify, render_template

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

@app.route('/details')
def Details():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
