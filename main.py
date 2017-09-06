from flask import Flask, flash, redirect, render_template, request, session, url_for
import pandas as pd
from predictor import TacPredictor
import csv

# Constants

featurelist = ['1','2','3','4','5','6','7','8','9','move']
datasetCSV = "tactacset.csv"

# App Config

app = Flask(__name__)
app.config.from_object('config')

TacPlayer = TacPredictor(featurelist,datasetCSV)

@app.route('/')
def home():
	return render_template('templates/index.html')

@app.route('/add',methods=["GET","POST"])
def addDataPoint():
	if request.method == "GET":
		return render_template("templates/add.html")
	if request.method == "POST":

@app.route("/viewDataset",methods=["GET"])
