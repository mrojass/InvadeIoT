from flask import Flask, jsonify, url_for, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/level1',methods=['POST','GET'])
def level1():
	return render_template('level1.html')

@app.route('/commands/<command>')
def commands(command):
	return command

if __name__ == "__main__":
	app.run(debug=True)