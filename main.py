from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):

    return "You're Pass with marks " + str(score)

    

@app.route('/fail/<int:score>')
def fail(score):
    return "You're Fail with marks " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result= ''
    if marks <50:
        result = 'fail'
    else:
        result= 'success'
    #return redirect(url_for(result, score = marks))    #this code has unique way to dispaly result
    return render_template('result.html', result= marks)       #this code also has unique way to dispaly result


@app.route('/submit', methods= ['POST',"GET"])
def submit():
    total_score= 0
    if request.method == 'POST':
        science= float(request.form['science'])
        maths= float(request.form['maths'])
        english= float(request.form['english'])
        total_score =(science + maths + english)/3

    return redirect(url_for('results', marks = total_score))

    # return "You're Fail with marks " + str(score)

if __name__ == "__main__":
    app.run(debug = True)