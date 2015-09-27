from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/level_one')
def level_one():
	return render_template("level_one.html")

@app.route('/level_two')
def level_two():
	return render_template("level_two.html")

if __name__ == "__main__":
	app.run(debug=True)