from flask import Flask

UPLOAD_FOLDER = "D:/Education & Job Related & Personal Info/Job Related/Bootcamp/Metis/edm_generator/flask-web-apps/upload"


# app = Flask(__name__, template_folder='templates\webaudiofont-master\examples')
app = Flask(__name__, template_folder='templates')
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
