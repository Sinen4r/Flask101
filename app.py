from flask import Flask 
app=Flask(__name__)


#wsgi Application

@app.route('/')
def welcome():
    return "Welcome to my website ss"



@app.route('/members')
def welcome():
    return "xxxxxxxxxxxxxxxxx"





if __name__ =='__main__':
    app.run(debug=True) 