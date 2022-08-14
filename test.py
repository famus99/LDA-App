import requests
from flask import Flask, render_template, request 
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


x = {'customer_ID': 'customer_id', 'time': 'order_date', 'count': 'payment', 'timeframe': 'hours', 'category_number': '5'}
print(x.keys())
