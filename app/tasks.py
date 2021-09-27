''' Tasks related to our celery functions '''

import time
import random
import datetime

from io import BytesIO
from celery import Celery, current_task
from celery.result import AsyncResult

from PIL import Image  
import os
import time

REDIS_URL = 'redis://redis:6379/0'
BROKER_URL = 'amqp://admin:mypass@rabbit//'

CELERY = Celery('tasks',
                backend=REDIS_URL,
                broker=BROKER_URL)

CELERY.conf.accept_content = ['json', 'msgpack']
CELERY.conf.result_serializer = 'msgpack'

def get_job(job_id):
    '''
    Ponto para ser chamado pelo web app e retorna o binario do .png
    '''
    return AsyncResult(job_id, app=CELERY)

@CELERY.task()
def image_demension(img):
    time.sleep(2)
    im = Image.open(img)  
    width, height = im.size

    # Redimensiona a imagem para 384x384  \
    im1 = im
    newsize = (384, 384) 
    im1 = im1.resize(newsize) 
    width, height = im1.size  
    location=os.path.join('static/worker-img','red_img.'+im.format.lower())
    im1.save(os.path.join('static/worker-img','red_img.'+im.format.lower()))   
    print(width,height)
    print("pass")

    return location
