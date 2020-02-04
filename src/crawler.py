from flask import Flask, request, jsonify
from src.page import github
app = Flask(__name__)



@app.route("/api/github", methods=["POST"])
def tags():
    data = request.json

    required = ["keywords", "proxies", "type"]
    for r in required:
        if not r in data:
            return jsonify(f'Bad request: {r} missed parameter'), 400
    
    types = ['Repositories', 'Wikis', 'Issues']
    correct_type = False
    for t in types:
        if t in data['type']:
            correct_type = True

    if not correct_type:
        return jsonify(f'Bad request: Invalid type {t}'), 400

    # Extra information
    extra = False
    if 'extra' in data and data['extra'] == True:
        extra = True

    error, result = github.get_query(data['keywords'], data['proxies'], data['type'], extra)
    
    if error:
        return jsonify(result), 500

    return jsonify(result), 200
    

@app.route("/")
def main():
    return "Github request"