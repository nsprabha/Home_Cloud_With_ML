from flask import Flask, render_template, request,redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
# Specify the upload directory
app.config['UPLOAD_FOLDER'] = 'C:/Users/NSPra/OneDrive/Desktop'
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/upload')
def upload_form():
    return render_template('upload.html')

@app.route('/uploader', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return 'No selected file'

        if file:
            # Ensure the filename is secure
            filename = secure_filename(file.filename)
            # Save the file to the upload directory
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)


"""
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/mainpage', methods=['POST'])

def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'pdfFile' not in request.files:
            return 'No file part'
        file = request.files['pdfFile']
        # If the user does not select a file, the browser submits an empty file without a filename
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)

    """

















"""
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Updated database URI
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    return 'User registered successfully'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return 'Login successful'
    else:
        return 'Invalid username or password'

if __name__ == '__main__':
    app.run(debug=True)


# 2nd comment code
from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app= Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLAlchemy_DATABASE_URI']='sqlite:///database.db'
app.config['SECRET_KEY']='thisisasecretkey'


class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    password=db.Column(db.String(20), nullable=False)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
if __name__=="__main__":
    app.run(debug=True)
    """