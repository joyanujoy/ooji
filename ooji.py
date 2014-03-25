# -*- coding: utf-8 -*-
"""
    ooji.py : main controller
"""
import model
import sys
import json
from urllib2 import quote, unquote
from bottle import Bottle, run, view, template, request, redirect
from encoder import Encoder

if len(sys.argv) < 2:
    raise RuntimeWarning("Usage python ooji.py <settings.json>")

HOST = '127.0.0.1'
config_file = sys.argv[1]

with open(config_file, 'r') as f:
    settings = json.load(f)

model = model.Model(**settings)
encoder = Encoder()

app = Bottle()


@app.route('/')
@view('home')
def home():
    return template('home')


@app.post('/shorten')
def shorten(hostname=HOST):
    url_fmt = "http://{host}/{path}"
    url = request.forms.get('url')
    safe_url = quote(url)
    req_id = model.add_url(safe_url)
    short_id = encoder.encode(req_id)
    return url_fmt.format(host=hostname, path=short_id)


@app.route('/<short_id:re:[a-zA-Z0-9]+>')
def expand(short_id):
    req_id = encoder.decode(short_id)
    url = model.query_url(req_id)
    plain_url = unquote(url)
    redirect(plain_url, 302)


@app.route('/options')
def options():
    pass


run(app, host='localhost', port=8080)
