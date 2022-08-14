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

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template('home.html')

if __name__ == "__main__":
    app.run()