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
    #p.grid.grid_line_alpha = 0
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = '%s Price' % ticker
    

    #.circle(x, y, size = 4, legend = ticker, color = 'darkgrey', alpha = 0.2)
    p.line(x, y, line_width=3, line_alpha=0.6, color = 'red', alpha = 0.6)
    

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

    plot = create_figure(ticker)

    if plot is None:
        return 'Plot not found'
    else:
        script, div = components(plot)

        return render_template('plot.html', script = script, div = div, ticker = ticker) 







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(port=33507)


