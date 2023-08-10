from flask import Flask, render_template,jsonify
import matplotlib.pyplot as plt
from datetime import datetime
import requests
import pandas as pd

def get_sterms(industry: str):
    call_django_api = 'http://127.0.0.1:8000/electricity_prediction/shortterm/'

    try:
        if(industry == 'ind1'):    
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            data = df[df['industry'] == '民生工業'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind2'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            data = df[df['industry'] == '石化業'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind3'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            data = df[df['industry'] == '金屬製造'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind4'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            data = df[df['industry'] == '資訊電子'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind5'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            data = df[df['industry'] == '綜合服務'].to_dict('records')
            # data = data[:24]
            return data
    except requests.exceptions.RequestException as e:
        jsonify({'error': str(e)})

def get_lterms(industry: str,time: str):
    call_django_api = 'http://127.0.0.1:8000/electricity_prediction/longterm/'
    
    try:
        if(industry == 'ind1'):    
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
            df =df[df['time'].dt.strftime('%Y-%m') == time]
            data = df[df['industry'] == '民生工業'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind2'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
            df =df[df['time'].dt.strftime('%Y-%m') == time]
            data = df[df['industry'] == '石化業'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind3'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
            df =df[df['time'].dt.strftime('%Y-%m') == time]
            data = df[df['industry'] == '金屬製造業'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind4'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
            df =df[df['time'].dt.strftime('%Y-%m') == time]
            data = df[df['industry'] == '資訊電子'].to_dict('records')
            # data = data[:24]
            return data
        elif(industry == 'ind5'):
            response = requests.get(call_django_api)
            data = response.json()
            df = pd.DataFrame(data)
            df['time'] = pd.to_datetime(df['time'],format='%Y/%m/%d')
            df =df[df['time'].dt.strftime('%Y-%m') == time]
            data = df[df['industry'] == '綜合服務業'].to_dict('records')
            # data = data[:24]
            return data
    except requests.exceptions.RequestException as e:
        jsonify({'error': str(e)})
   
# 沒用到     
def plot_chart(data: list, industry: str):
    # 決定圖表標題
    if(industry == 'ind1'):
        ind_title = '民生工業'
    elif(industry == 'ind2'):
        ind_title = '石化業'
    elif(industry == 'ind3'):
        ind_title = '金屬製造'
    elif(industry == 'ind4'):
        ind_title = '資訊電子'
    elif(industry == 'ind5'):
        ind_title = '綜合服務'
          
    
    # 提取時間和電力預測數據
    times = [datetime.strptime(entry['time'], '%Y-%m-%dT%H:%M:%SZ') for entry in data]
    electricity_predicts = [entry['electricity_predict'] for entry in data]

    # 創建折線圖
    plt.figure(figsize=(10, 6))
    plt.plot(times, electricity_predicts, marker='o')

    # 添加標題和軸標籤
    plt.title('Electricity Predictions')
    plt.xlabel('Time')
    plt.ylabel('Electricity Predictions')

    # 自動調整日期標籤，以避免重疊
    plt.gcf().autofmt_xdate()

    # 顯示圖表
    plt.tight_layout()
    # plt.show()
    plt.draw()
    plt.savefig('static/output_img/shortterm.png')
   
def plot_shorttrem(data: list, industry: str):
    if(industry == 'ind1'):
        df = pd.DataFrame(data)
        data = df[df['industry'] == '民生工業'].to_dict('records')
        data = data[:24]
        plot_chart(data, industry)
    elif(industry == 'ind2'):
        df = pd.DataFrame(data)
        data = df[df['industry'] == '石化業'].to_dict('records')
        data = data[:24]
        plot_chart(data,industry)
    elif(industry == 'ind3'):
        df = pd.DataFrame(data)
        data = df[df['industry'] == '金屬製造'].to_dict('records')
        data = data[:24]
        plot_chart(data,industry)
    elif(industry == 'ind4'):
        df = pd.DataFrame(data)
        data = df[df['industry'] == '資訊電子'].to_dict('records')
        data = data[:24]
        plot_chart(data,industry)
    elif(industry == 'ind5'):
        df = pd.DataFrame(data)
        data = df[df['industry'] == '綜合服務'].to_dict('records')
        data = data[:24]
        plot_chart(data,industry)