from flask import Flask, request, jsonify
from src.github import github
from src.errors import TypeOfError
app = Flask(__name__)



@app.route("/api/github", methods=["POST"])
def tags():
    data = request.json

    t_error, content = github.search(data)
    if t_error == TypeOfError.einput:
        return jsonify(f'Bad request: {t_error.name}'), 400
    elif t_error == TypeOfError.erequest:
        return jsonify(f'Internal error: {t_error.name}'), 500

    return jsonify(content), 200
    

@app.route("/")
def main():
    return "Github request"