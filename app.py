# Integrating HTML with flask

from flask import Flask,request,redirect,url_for

app = Flask(__name__)

#@app.route('/')
#def index():
#    user_agent = request.headers.get('User-Agent')
#    return "Your Browser is "+user_agent

###########################

from flask import render_template ## Used to render the html page
@app.route('/')
def welcome():
    return render_template('index.html')

###########################

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res='Passed'
    else:
        res='Failed'
    return render_template('result.html',result=res)

@app.route('/checker/<int:score>')
def checker(score):
    if score>=50:
        res='PASS'
    else:
        res='FAIL'
    exp={'score':score,'result':res}
    return render_template('result.html',result=exp)
###########################

# Result checker submit HTML page
# To read posted value we have to import request function

from flask import request
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    return redirect(url_for("checker",score=total_score))

###########################

## Redirect function, Result checker
from flask import redirect,url_for
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks < 50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

############################

## Response function
from flask import make_response
@app.route('/')
def index():
    response = make_response('<h1> this document carries a cookie! </h1>')
    response.set_cookie('answer','42')
    return response
if __name__ == '__main__':
    app.run(debug=True)
    

