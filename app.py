# importing dependencies
from predict import get_no
from url import api
import glob
import os
import cv2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


app = Flask(__name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

BASE_DIR = os.getcwd()
dir = os.path.join(BASE_DIR, "uploads")

for root, dirs, files in os.walk(dir):
    for file in files:
        path = os.path.join(dir, file)
        os.remove(path)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def index():
    return render_template('try.html')

# Prediction - Vehicle Details Page


@app.route('/vehicle', methods=['GET', 'POST'])
def inde():
    target = os.path.join(UPLOAD_FOLDER, '')
    message = request.form['message']
    if not os.path.isdir(target):
        os.makedirs(target)
    if request.method == 'POST':
        file = request.files['file']
        file_name = file.filename or ''
        destination = ''.join([target, file_name])
        file.save(destination)
        number = get_no(destination)
        api(number , message , destination)
        BASE_DIR = os.getcwd()
    dir = os.path.join(BASE_DIR, "uploads")

    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(dir, file)
            os.remove(path)
    return render_template('done.html')


