from flask import Flask, render_template, request, flash, redirect, session, g, url_for
import os


app = Flask(__name__)
app.secret_key = "comia"

@app.route('/', methods= ['GET', 'POST'])
def homepage():
	if request.method == 'POST':
		session.pop('user', None)

		if request.form['password'] == 'football':

			session['user'] = request.form['username']
			return redirect(url_for('index'))
	return render_template('homepage.html')

@app.before_request
def before_request():
	g.user = None

	if 'user' in session:
		g.user = session['user']



@app.route("/welcome")
def index():
	if g.user:
		flash("Welcome to football fitness!")
		return render_template("index.html", user = session['user'])
	return redirect(url_for('homepage'))
@app.route("/begin", methods=['POST', 'GET'])


def begin():
	flash("What is your name?")
	return render_template("info.html")


@app.route("/submit", methods=['POST', 'GET'])

def submit():
	if request.form['position'] == 'GK' and request.form['difficulty']== 'Easy':


		return render_template('GKeasy.html')


	if request.form['position'] == 'GK' and request.form['difficulty']== 'Medium':


		return render_template('GKmedium.html')

	if request.form['position'] == 'GK' and request.form['difficulty']== 'Hard':


		return render_template('GKhard.html')

	if request.form['position'] == 'DEF' and request.form['difficulty']== 'Easy':


		return render_template('DEFeasy.html')

	if request.form['position'] == 'DEF' and request.form['difficulty']== 'Medium':


		return render_template('DEFmedium.html')

	if request.form['position'] == 'DEF' and request.form['difficulty']== 'Hard':


		return render_template('DEFhard.html')

	if request.form['position'] == 'MID' and request.form['difficulty']== 'Easy':


		return render_template('MIDeasy.html')

	if request.form['position'] == 'MID' and request.form['difficulty']== 'Medium':


		return render_template('MIDmedium.html')

	if request.form['position'] == 'MID' and request.form['difficulty']== 'Hard':


		return render_template('MIDhard.html')

	if request.form['position'] == 'STR' and request.form['difficulty']== 'Easy':


		return render_template('STReasy.html')

	if request.form['position'] == 'STR' and request.form['difficulty']== 'Medium':


		return render_template('STRmedium.html')





	if request.form['position'] == 'STR' and request.form['difficulty']== 'Hard':


		return render_template('STRhard.html')








