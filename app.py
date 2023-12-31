from flask import Flask, render_template,jsonify,request,url_for
from jinja2 import Template
import requests
import estimate
import testing


app = Flask(__name__) # 代表目前執行的模組

@app.route('/') # 函式的裝飾(Decorator): 以函式為基礎，提供附加功能
def index():
    industry = request.form.get('industry')
    print('------------------')
    print(industry)
    return render_template('index.html')

@app.route('/test',methods=['GET','POST']) # 代表我們要處理的路徑
def test():
    data = estimate.get_sterms(industry='ind3')
    return render_template('jstest.html',data=data[:24]) #24小時data

@app.route('/envintro')
def envintro():
    return render_template('envintro.html')

@app.route('/teamintro')
def teamintro():
    return render_template('teamintro.html')

@app.route('/shortterm_est', methods=['GET','POST'])
def get_shortterm_and_plot():
    industry = request.form.get('industry')
    # print('------------------')
    # print(industry)
    start = int(request.args.get('start', 120))  
    end = int(request.args.get('end', 145)) 
    data = estimate.get_sterms(industry=industry)
    new_start = start + 24  # 计算新的 start 值
    new_end = end + 24  # 计算新的 end 值
    return render_template('estimate_shortterm.html',data=data[start:end],industry=industry, start=start, end=end) #24小時data12
    

@app.route('/longterm_est', methods=['GET','POST'])
def get_longterm_and_plot():
    industry = request.form.get('industry')
    time = request.form.get('start')
    data = estimate.get_lterms(industry=industry,time=time)
    # estimate.plot_shorttrem(data, industry)
    return render_template('estimate_longterm.html',data=data) 

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0')