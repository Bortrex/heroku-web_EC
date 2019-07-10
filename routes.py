from flask import render_template

from __init__ import app

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')\

# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return render_template('500.html'), 500

@app.route('/definitions')
def definitions():
    return render_template('definitions.html')

@app.route('/upload')
def upload_form():
    return render_template('upload.html')

# TODO: each of us must define our template and further things..
@app.route('/francesco')
def fran():
    return render_template('francesco.html')

@app.route('/judicael')
def judi():
    return render_template('judicael.html')

@app.route('/samy')
def sam():
    return render_template('samy.html')