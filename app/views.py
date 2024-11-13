from flask import Blueprint, redirect, url_for, request, render_template, flash, get_flashed_messages, current_app, jsonify
from werkzeug.utils import secure_filename
from .forms import fileSubmissionForm
from .Utils.ReadLang import readJson
import os
views = Blueprint('views', __name__)

# Add this route to redirect from the root ("/") to "/auth/login" eventually move to a standard views.py file
@views.route('/', methods=['GET'])
def root():
    return redirect(url_for('authviews.login'))

@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = fileSubmissionForm()
    fileType = ""

    if request.method == 'POST':
        # Debugging: check what's inside request.files
        if not request.files:
            flash('No files found in the request.', 'error')
            return redirect(request.url)

        # Check if the POST request has the file part
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, the browser submits an empty file without a filename.
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)

        # Secure the filename and save the file to the specified folder
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        # You can process the file here (e.g., reading the file or extracting its type)
        filesplit = filename.split('.')
        fileType = readJson(filename)  # If you want to process the file further
        flash('File successfully uploaded', 'success')
        
        return render_template('dashboard.html', form=form, fileType=fileType, fileName=filename)
    else:
        return render_template('dashboard.html', form=form)