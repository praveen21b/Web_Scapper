from crypt import methods
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import requests
import csv

app = Flask(__name__) # Creating object of flask class
# name of the application package, helps flask to identify 
# resources (templetes, static assets, istance folders)

@app.route('/', methods = ['GET '])
def rendering_homepage():
    #return render_template('index.html')
    pass

@app.route('/review', methods = ['GET', 'POST'])
def show():
    try:
        pass
    except Exception as e:
        pass