from flask import Flask,render_template,request
import pandas as pd
import os
app = Flask('test123')
UPLOAD_FOLDER = 'static/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  #giving a folder to save the file
@app.route('/',methods=['GET','POST'])
def basic():
    return render_template('index.html')
@app.route('/data',methods=['GET','POST'])
def uploadFiles():
    uploaded_file = request.files['nfile']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
    uploaded_file.save(filepath)
    data = pd.read_csv(filepath,delimiter='\t')
    return render_template('data.html',data=[data.to_html(),uploaded_file.filename,filepath])

if __name__ == '__main__':
    app.run()