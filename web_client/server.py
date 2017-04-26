import os
from flask import Flask, render_template
import jinja2

server = Flask(__name__,
               static_url_path="",
               static_folder="static")

@server.route("/", defaults={ "path": "index" })
@server.route("/<path>")
def serve_file(path):
    return render_template('.'.join([path, "html"]))

@server.errorhandler(404)
@server.errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(error):
    return "Nope.", 404

if __name__ == "__main__":
    server.run("0.0.0.0", port=8080, debug=True)