# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 11:36:15 2020

@author: RQML4978
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/sound_design')
def sound_design():
    return render_template('sound_design.html')

@app.route('/about')
def about():
    return render_template('index.html')