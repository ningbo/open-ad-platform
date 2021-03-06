from flask import render_template
from app import app
from app import models
import random

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/ad')
def get_ad():
    ad = random.choice(models.Advertisement.query.all())
    return render_template('ad.html', **ad.render())

@app.route('/adscript')
def ad_script():
    return app.send_static_file('js/ad.js')

@app.after_request
def allow_cross_origin_requests(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
