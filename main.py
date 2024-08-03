#integrate html with flask
from flask import Flask ,redirect,url_for,render_template,request
app=Flask(__name__)


#wsgi Application

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/sucess/<int:score>')
def sucess(score):
    return "the person has passed and the mark is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    res=""
    if score>60:
        res="PASS"
    else:
        res='FAIL'
    exp={'score':score,'res':res}
    return render_template('results.html',result=exp)


@app.route('/results/<int:marks>')
def results(marks):
    if marks>60:
        results='sucess'
    else:
        results='fail'
    return redirect (url_for(results,score=marks))

@app.route('/submit',methods=['POST','GET'])
def submit ():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+math+c+data_science)/4
    
    return redirect (url_for('fail',score=total_score))

if __name__ =='__main__':
    app.run(debug=True) 