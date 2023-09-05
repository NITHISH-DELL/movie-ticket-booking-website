from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to the world"

@app.route('/success/<int:score>')
def success(score):
    return 'You are passed the exam ' + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Sorry!! you have failed the exam " + str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
    
    return redirect(url_for(result,score = marks))


if __name__ == '__main__':
    app.run(debug = True)

