from flask import Flask, render_template, request, redirect, url_for, send_file
from assets import decrypt, encrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return redirect(url_for('home'))


@app.route('/home')
def home():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        password = request.form['text']
        encrypted_file = encrypt.encrypt_pdf(f, password)
        return send_file(encrypted_file, download_name=f.filename, mimetype=f.mimetype, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
