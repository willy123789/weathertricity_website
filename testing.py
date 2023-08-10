from flask import Flask, render_template,jsonify
from jinja2 import Template
import requests
import estimate
import pandas as pd
import mplcursors

call_django_api = 'http://127.0.0.1:8000/electricity_prediction/longterm/'
response = requests.get(call_django_api)
data = response.json()

df = pd.DataFrame(data)
time = '2023-08'
df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
df =df[df['time'].dt.strftime('%Y-%m') == time]
df = df[df['industry'] == '金屬製造業']
print(df.head())

# data = estimate.get_lterms(industry='ind3',time='2023-08')
# data = estimate.get_lterms(industry='ind3',time='2023-09')
# df = df = pd.DataFrame(data)
# # print(df.head())
# df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
# df2 =df[df['time'].dt.strftime('%Y-%m') == '2023-08']
# print(data)