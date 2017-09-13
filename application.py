from flask import Flask, flash, redirect, render_template, request, url_for
import pandas as pd
from predictor import TacPredictor
import csv

# Constants

featurelist = ['1','2','3','4','5','6','7','8','9','move']
datasetCSV = "tactacset.csv"

# App Config

app = Flask(__name__)
app.config['DEBUG'] = True

TacPlayer = TacPredictor(featurelist,datasetCSV)

# Prevent caching
@app.after_request
def add_header(r):
  """
  Add headers to both force latest IE rendering engine or Chrome Frame,
  and also to cache the rendered page for 10 minutes.
  """
  r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
  r.headers["Pragma"] = "no-cache"
  r.headers["Expires"] = "0"
  r.headers['Cache-Control'] = 'public, max-age=0'
  return r

@app.route('/',methods=["GET"])
def home():
  return render_template('board.html')

@app.route('/add',methods=["GET","POST"])
def addDataPoint():
  if request.method == "GET":
    # Can manually add datapoint(s) from here
    return render_template("add.html")
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