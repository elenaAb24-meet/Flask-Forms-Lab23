from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "elenaab"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]


@app.route('/')  # '/' for the default page
def login():
  return render_template('login.html')

  @app.route('/create', methods=['GET', 'POST'])
def homepage():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['firstname']
        animal = request.form['animal']

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
