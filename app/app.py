from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/test')
def test():
	return render_template('text.html')

if __name__ == "__main__":
	app.run(debug=True)