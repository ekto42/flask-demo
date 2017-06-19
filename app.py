from flask import Flask, render_template, request, redirect

import datetime

import quandl as qd
import pandas as pd
import requests


from bokeh.plotting import figure
from bokeh.embed import components

app = Flask(__name__)


today = datetime.date.today()
start_date = today - datetime.timedelta(days = 90)

api_key = 'bB5qXVs1HejzVsWA8bJx'

def request_data(ticker):
    df = qd.get('WIKI/%s' % ticker, trim_start = start_date, trim_end = today)
    df = df[['Open','Close','Adj. Open','Adj. Close']].reset_index()
    return df
    #search_url = "https://www.quandl.com/api/v3/datasets/WIKI/%s/data.json?api_key=%s&start_date=%s&end_date=%s"%(ticker,api_key,start_date,today)
    
def create_figure(ticker):
    df = request_data(ticker)
    x = df['Date']
    y = df['Open']

    p = figure(x_axis_type="datetime", title="%s Closing Prices" % ticker)
    p.grid.grid_line_alpha = 0
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = '%s Price' % ticker
    p.ygrid.band_fill_color = "green"
    p.ygrid.band_fill_alpha = 0.1

    p.circle(x, y, size = 4, legend = ticker, color = 'darkgrey', alpha = 0.2)

    p.legend.location = "top_left"
    return p


@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    ticker = request.form['ticker']
    #price = request.form['price']


    #return str(ticker)

    plot = create_figure(ticker)

    if plot is None:
        return 'Plot not found'
    else:
        script, div = components(plot)

        return render_template('plot.html', script = script, div = div, ticker = ticker) 







if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0')
    app.run(port=33507)




'''
@app_lulu.route('/index_lulu', methods=['GET','POST'])
def index_lulu():
    nquestions = 5
    if request.method == 'GET':
        return render_template('userinfo_lulu.html', num = nquestions)
    else:
        #request was a post
        app_lulu.vars['name'] = request.form['name_lulu']
        app_lulu.vars['age'] = request.form['age_lulu']

        f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'w')
        f.write('Name: %s\n'%(app_lulu.vars['name']))
        f.write('Age: %s\n\n'%(app_lulu.vars['age']))
        f.close()

        return redirect('/main_lulu')

@app_lulu.route('/main_lulu')
def main_lulu2():
    if len(app_lulu.questions)==0 : return render_template('end_lulu.html')
    return redirect('/next_lulu')

@app_lulu.route('/next_lulu', methods=['POST'])
def next_lulu():
    return redirect('/usefulfunction_lulu')

@app_lulu.route('/usefulfunction_lulu',methods=['GET','POST'])
def usefulfunction_lulu():    
    return render_template('layout_lulu.html', num =1, question = 'Which fruit do you like best?',ans1='banana',\
        ans2='mango',ans3='pineapple')
'''
