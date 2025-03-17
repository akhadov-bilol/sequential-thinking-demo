from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello, Sequential World!'})

@app.route('/greet/<name>')
def greet_user(name):
    return jsonify({'message': f'Hello, {name}! Welcome to our API!'})

if __name__ == '__main__':
    app.run(debug=True)