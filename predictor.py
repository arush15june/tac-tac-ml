import pandas as pd 
import numpy as np
from sklearn import linear_model
from sklearn import Pipeline
from sklearn import preprocessing
from sklearn.externals import joblib

class TacPredictor:

  """
    For our tic tac toe board:
    X : shape=[n,9]
        9 features having values {-1,0,1} where 
                    -1 := "Empty" 
                     0 := "O" 
                     1 := "X"
        representing each position on the board
    Y :   
        9 classes representing each position on the board. 
        The column vector representing representing Y is assumed 
        to be the last column of the input dataset.

  """


  model = Pipeline(steps=[('logreg',linear_model.LogisticRegression())])

  def __init__(self,features,datafile):
    self.datafile = datafile
    self.dataset = pd.DataFrame(np.array([]),columns=features)
    self.featureN = len(features)
    self.dataN = len(dataset)
    
  def addPoint(row):
    self.dataset.append(row)

  def loadDataset():
    self.dataset = pd.read_csv(datafile)

  def saveDataset():
    self.dataset.to_csv(datafile)
  
  def fit():
    """
      Extract Feature Vectors X and Output Vector y from 
      Raw Dateset;
      Assumption : Output Vector y is always the last column of
      the dataset
    """
    dataset_DF_X = self.dataset[features[:-1]]
    dataset_DF_Y = self.dataset[features[-1:]]

    """
      Split dataset into 
      80% Training Set 
      and
      20% Test Set
    """
    train_DF_X = dataset_DF_X[:-0.2*dataN] 
    train_DF_Y = dataset_DF_Y[:-0.2*dataN] 

    test_DF_X = dataset_DF_X[-0.2*dataN:]
    test_DF_Y = dataset_DF_Y[-0.2*dataN:]

    # Train the model
    model.fit(train_DF_X,train_DF_Y)

    metrics = { 'accuracyscore' : model.score(test_DF_X,test_DF_Y) }
    
    return metrics
  
  def predict(board):
    return model.predict(board)

  def saveModel(filename):
    joblib.dump(model,"{}.pkl".format(filename))

  def loadModel(filename):
    model = joblib.load("{}.pkl".format(filename))
