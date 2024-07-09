from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api')
def api():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return jsonify({
        "bo": data
    })

if __name__ == '__main__':
    app.run(debug=True)
