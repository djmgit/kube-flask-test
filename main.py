from flask import Flask, redirect, url_for, request, jsonify, render_template
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = "THIS IS SECRET"

branch = "dev"

@app.route("/app")
def index():
	return 'Hellow world! I am on branch {}'.format(branch)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=7070)

