from tkinter import Variable
import requests
from flask import Flask, render_template, request ,redirect, url_for
import requests
import os
import json
import pandas as pd
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, minmax_scale
import os
import matplotlib.pyplot as plt
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from sklearn.decomposition import LatentDirichletAllocation as LDA
import csv



app = Flask(__name__)
app.config['SECRET_KEY'] = 'Blessing99..'
app.config['UPLOAD_FOLDER'] = 'static/files'
# app.config['SEND_FILE_MAX_AGE_DEFAULT']

# %matplotlib inline 

class UploadFileForm(FlaskForm):
    file = FileField("File")
    
    submit = SubmitField("Upload File")

@app.route("/", methods = ["GET","POST"])
def home():
  return render_template('index.html')

@app.route("/Output", methods = ["GET","POST"])
def Output():
  return render_template('Output.html')


@app.route("/Instruction", methods = ["GET","POST"])
def Instruction():
  return render_template('Instruction.html')


@app.route("/Submit", methods = ["GET","POST"])
def Submit():
  form = UploadFileForm()
  if form.validate_on_submit():
      file = form.file.data 
      file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
      return redirect(url_for('submit2'))

  return render_template('Submit.html',form = form)

@app.route("/submit2")
def submit2():
  uploaded_file = os.listdir('C:/Users/samto/Documents/GitHub/web_app/static/files')[0]
  df1 = pd.read_csv('C:/Users/samto/Documents/GitHub/web_app/static/files/' + '{0}'.format(uploaded_file))
  Variable = []
  for col in df1.columns:
    Variable.append(str(col))
  # var = str(column_list)
  return render_template('Submit2.html',Variable = Variable)

@app.route('/test',methods = ['POST'])
def test2():
  output = request.get_json()
  result = json.loads(output)
  customer_id = result['customer_ID']
  time = result['time']
  count = result['count']
  category_number = result['category_number']
  timeframe = result['timeframe']
  uploaded_file = os.listdir('C:/Users/samto/Documents/GitHub/web_app/static/files')[0]
  df1 = pd.read_csv('C:/Users/samto/Documents/GitHub/web_app/static/files/' + '{0}'.format(uploaded_file))
  df1[str(time)] = pd.to_datetime(df1[str(time)])
  print(df1['order_date'])
  df_pivot = pd.pivot_table(df1, index='{}'.format(customer_id), columns='{}'.format(time), values= '{}'.format(count),fill_value= 0)
  if timeframe == 'hours':
    df_avg = df_pivot.T.groupby(df_pivot.T.index.hour).mean().T
  elif timeframe == 'days':
    df_avg = df_pivot.T.groupby(df_pivot.T.index.day).mean().T
  elif timeframe == 'weeks':
    df_avg = df_pivot.T.groupby(df_pivot.T.index.week).mean().T
  elif timeframe == 'months':
    df_avg = df_pivot.T.groupby(df_pivot.T.index.month).mean().T
  elif timeframe == 'years':
    df_avg = df_pivot.T.groupby(df_pivot.T.index.year).mean().T

  lda = LDA(n_components= int(category_number), learning_method='batch')

  lda = lda.fit(df_avg)

  df_comp = pd.DataFrame(lda.components_.T, index=df_avg.columns)
  norm_components = lda.components_ / lda.components_.sum(axis=1)[:, np.newaxis]
  df_comp_norm = pd.DataFrame(norm_components.T, index=df_avg.columns)
  df_avg['cluster'] = np.argmax(lda.transform(df_avg), axis=1)
  arr = df1['customer_id'].to_numpy()
  arr = list(arr)
  df_avg2 = df_avg.reset_index()

  def get_idx(val):
    index = df_avg2.index

    condition = df_avg2["customer_id"] == val

    specific_index = index[condition]

    ID_indices_list = specific_index.tolist()

    return ID_indices_list[0]

  def topic_1(customerid):

    formatter = "{:.2%}".format
    sample = df_avg.iloc[get_idx(customerid),:-1]
    perc = lda.transform(np.array(sample).reshape(1, -1))

    return list(perc)

  def topic(customerid):
    
    formatter = "{:.2%}".format
    sample = df_avg.iloc[get_idx(customerid),:-1]
    perc = lda.transform(np.array(sample).reshape(1, -1))

    data = np.array([formatter(x) for x in perc[0]])
    final = pd.DataFrame(data, columns=['%'])
    # final['maxv'] = final.apply(max,axis = 1)
    # final['con'] = final.idxmax(axis = 1)
    final['%'] = final['%'].str.rstrip('%').astype('float')/100
    i = final['%'].idxmax()
    
    return i
  
  output = []
  count = 0
  for i in arr:
    output.append([i,topic(i),list(get_idx(topic_1(i)))[0]])

  with open('C:/Users/samto/Documents/GitHub/web_app/static/files/output.csv','w') as out:
    writer = csv.writer(out)
    writer.writerow(['Customer ID','category','Probability'])
    for i in output:
      
      writer.writerow(i)
    out.close
  return redirect(url_for('Output.html'))

if __name__ == "__main__":
  app.run(port = 5001)