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
  return render_template('templates/board.html')

@app.route('/add',methods=["GET","POST"])
def addDataPoint():
  if request.method == "GET":
    # Can manually add datapoint(s) from here
    return render_template("templates/add.html")
  elif request.method == "POST":
    # Get the board data sent as a json in the format :
    # { '1' : 0, '2' : -1, '3' : 1,.....,'9' : '0','move' : '7' }
    board_JSON = request.get_json()
    board = []
    for key,val in board_JSON:
      board.append(val)

    TacPlayer.addPoint(board)
    return jsonify({'success' : 1})
    
    
@app.route("/view/<selection>",methods=["GET"])
def viewer(selection):
  # <selection> : model, dataset
  return redirect(url_for('/'))

@app.route("/prediction",methods=["GET"])
def prediction():
  board_JSON = request.get_json()
  if not board:
    return jsonify({'error' : 'invalid board input'})
  x = []
  # Process JSON for predictor
  for key,val in board_JSON.items():
    if key == 'move':
      continue
    x.append(val)

  prediction = {}
  prediction['prediction'] = model.predict(x)
  return jsonify(prediction)