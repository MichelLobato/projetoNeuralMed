import json
from flask import Flask, request
from flask import render_template, make_response
import tasks
import os
from PIL import Image
from datetime import datetime

APP = Flask(__name__)
APP.config['UPLOAD_FOLDER'] = 'static/worker-img'

@APP.route('/',methods = ['GET','POST'])
def index(): 
    '''
    Renderiza o template, e pelo metodo post carrega imagem
    '''
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        img = request.files['image']
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        img.save(os.path.join(APP.config['UPLOAD_FOLDER'],img.filename))
        loc = "static/worker-img/"+img.filename
        job = tasks.image_demension.delay(loc)
        return render_template("download.html",JOBID=job.id)


@APP.route('/progress')
def progress():
    '''
    Get task e retorna usando um objeto JSON
    '''
    jobid = request.values.get('jobid')
    if jobid:
        job = tasks.get_job(jobid)
        if job.state == 'PROGRESS':
            return json.dumps(dict(
                state=job.state,
                progress=job.result['current'],
            ))
        elif job.state == 'SUCCESS':
            return json.dumps(dict(
                state=job.state,
                progress=1.0,
            ))
    return '{}'

@APP.route('/result.png')
def result():
    '''
    Get o binario do .png gerado no redis e return
    '''
    jobid = request.values.get('jobid')
    if jobid:
        job = tasks.get_job(jobid)
        png_output = job.get()
        png_output="../"+png_output
        return png_output
    else:
        return 404




if __name__ == '__main__':
    APP.run(host='0.0.0.0')
