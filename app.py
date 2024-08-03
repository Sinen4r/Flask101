from flask import Flask ,redirect,url_for,render_template
app=Flask(__name__)


#wsgi Application

@app.route('/')
def welcome():
    return "Welcome to my website ss"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "the person has passed and the mark is "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the mark is "+ str(score)


@app.route('/results/<int:marks>')
def results(marks):
    if marks>60:
        results='sucess'
    else:
        results='fail'
    return redirect (url_for(results,score=marks))



if __name__ =='__main__':
    app.run(debug=True) 