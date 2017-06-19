from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.vars={}

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
  return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    app.vars['ticker'] = request.form['ticker']
    # app.vars['closing_price'] = request.form['closing_price']
    # app.vars['adj_closing_price'] = request.form['adj_closing_price']
    # app.vars['opening_price'] = request.form['opening_price']
    # app.vars['adj_opening_price'] = request.form['adj_opening_price']
    


    return render_template('plot.html', ticker = app.vars['ticker']) 







if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    #app.run(port=33507)




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
