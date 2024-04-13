from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Specify the upload directory
app.config['UPLOAD_FOLDER'] = 'C:/Users/NSPra/OneDrive/Desktop'

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
