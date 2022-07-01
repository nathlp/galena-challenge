from flask import Flask, redirect, render_template, jsonify, request
from sqlalchemy.sql import text
from candidate_model import db, Candidate
import os
from werkzeug.utils import secure_filename
from openpyxl import load_workbook
import openpyxl.utils.dataframe 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:abc123@127.0.0.1/galenadb' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = '/home/nathalialp/github/galena-challenge/uploads/' 
db.init_app(app)

@app.before_first_request
def create_db():
    db.create_all()
    
@app.route('/')
def index():
    candidates = Candidate().list_all()
    return render_template('index.html', the_title="Lista de Candidatos", candidates=candidates) 


@app.route('/Candidate/create', methods=['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('upload.html', the_title="Upload Planilha")
    if request.method =='POST':
        fi = request.files['filename']
        fn = secure_filename(fi.filename)
        fi.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
        #return render_template('up.html', the_title="Upload Planilha", fn=fn)
        wb = load_workbook(os.path.join(app.config['UPLOAD_FOLDER'],fn))
        ws = wb.active
        ws.delete_rows(1, 4)
        #df = DataFrame(ws.values)

@app.route('/Candidate/update/<int:id>')
def update(id):
    candidate = Candidate().update(id)
    return redirect(request.referrer)

@app.route('/Candidate/delete/<int:id>')
def delete(id):
    candidate = Candidate()
    candidate.delete(id)
    return redirect(request.referrer)

@app.route('/teste')
def teste():
    return render_template('teste.html')


app.run() 
