from flask import Flask
import sys, os

# sys.path.append(os.getcwd() + "/_defs")
UPLOAD_FOLDER = os.getcwd() + '/uploads'

app = Flask(__name__)
app.secret_key = b'some secret word'#b'_5#y2L"F4Q8z\n\xec]/' # in order to use flashes messages

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # to limit the size of the file to 16mb
