import os
import urllib.request
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt'])#, 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


# from ..__init__.app import app
# from Testing_flask import app

from __init__ import app

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/defs')
def upload_form1(): # changed to '_form1' due to is messing with some default form
    return render_template('upload.html')

@app.route('/defs', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        ## check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')

            return redirect(request.url)
        file_s = request.files.getlist('file')#files['file']
        for file in file_s:
            if file.filename == '':
                flash('No file selected for uploading')

                return redirect(request.url)

            if file and not allowed_file(file.filename):
                flash('Please, Only allowed file types: *.txt')  # , pdf, png, jpg, jpeg, gif')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                task = "/definitions"
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'] + task, filename))

        flash('File(s) successfully uploaded!')
        return redirect('/defs')


@app.route('/appear')
def pass2reader():

    path = os.getcwd()+'/uploads/definitions'
    if not os.path.exists(path):
        os.makedirs(path)

    if not os.listdir(path):
        flash("Directory is empty!")
        return redirect('/defs')
    else:
        nb_files = len(os.listdir(path))
        flash("You succesfully uploaded {} files!!".format(nb_files))
        return redirect('/definitions')