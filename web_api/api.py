from flask import Flask, request, jsonify
from lib.parse_jpn_rpc import ParseJapaneseRpc

parse_jpn_rpc = ParseJapaneseRpc()

api = Flask(__name__.split('.')[0])

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
 