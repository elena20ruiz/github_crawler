from flask import Flask, request, jsonify
from src.page import github
app = Flask(__name__)



@app.route("/api/github", METHOD=["POST"])
def tags():
    data = request.json
    
    required = ["keywords", "proxy", "type"]
    for r in required:
        if not r in data:
            return jsonify(f'Bad request: {r} missed parameter'), 400
    
    if data['type'] == 'repositories':
        result = github.get_repositories(data['keywords'], data['proxy'])
    elif data['type'] == 'wikis':
        result = []
    elif data['type'] == 'issues':
        result = []
    else:
        return jsonify(f'Bad request: Invalid type parameter'), 400
    
    return jsonify(result), 200
    

@app.route("/")
def main():
    return "Github request"