from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.parse_jpn_rpc import ParseJapaneseRpc

from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper

parse_jpn_rpc = ParseJapaneseRpc()

api = Flask(__name__.split('.')[0])
cors = CORS(api, resources={
    r"/api/*": {
        "origins": "*"
    }
})

@api.route("/api/v1/parse")
def get_parsed_sentence():
    sentence = request.args.get("sentence")
    parsed = parse_jpn_rpc(sentence)
    return jsonify(parsed)

@api.errorhandler(404)
def page_not_found(error):
    return "This page does not exist.", 404

if __name__ == "__main__":
    api.run("0.0.0.0", port=5000, debug=True)
 