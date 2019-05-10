from flask import Flask, make_response, jsonify, request
from nlp.keyphrase_extractor import position_rank, topic_rank, text_rank
import os

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/keywords/position', methods=['POST'])
def get_position_rank():
    if not request.json or not 'content' in request.json:
        abort(400)
    keyphrases = position_rank(request.json['content'])
    return jsonify({'task': keyphrases}), 200

@app.route('/keywords/topic', methods=['POST'])
def get_topic_rank():
    if not request.json or not 'content' in request.json:
        abort(400)
    keyphrases = topic_rank(request.json['content'])
    return jsonify({'task': keyphrases}), 200

@app.route('/keywords/text', methods=['POST'])
def get_text_rank():
    if not request.json or not 'content' in request.json:
        abort(400)
    keyphrases = text_rank(request.json['content'])
    return jsonify({'task': keyphrases}), 200

@app.route('/internal/status', methods=['GET'])
def get_internal_status():
    return jsonify({"contact": {"phone-number": "+49 6221 345 4301"}}), 200

@app.route('/internal/version', methods=['GET'])
def get_internal_version():
    return jsonify({"origin": "git@github.com:springernature/prs-reviewers.git","link": "git@github.com:springernature/prs-reviewers.git","revision": "d9275f00ec768249bceb07302fd63fd82a7182e2","branch": "master"}), 200


def mount_web_app():
    port = int(os.getenv("PORT", 9099))
    
    app.run(host='0.0.0.0', port=port, debug=False) 
    


