from flask import Flask, render_template, request

app = Flask(__name__)

aka = [
    {
        'title':'Rohitha',
        'content':'Gundram'
    },
    {
        'title':'Bhanu',
        'content':'Banda Bhanu (BB)'
    }
]

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/predictionform', methods = ['POST'])
def getpred():
    car_name = request.form['carname']
    man_year = request.form['myear']
    odo_read = request.form['odo']
    return render_template('test.html', c=car_name, m=man_year, o=odo_read)

@app.route('/PricePrediction')
def proce():
    return render_template('PricePrediction.html', pred=aka)

''' @app.route('/predictionform')
def pred():
    return render_template('PredictionForm.html')

@app.route('/predictionform', methods = ['POST'])
def getpred():
    car_name = request.form['carname']
    man_year = request.form['myear']
    odo_read = request.form['odo']

    return render_template('test.html', c=car_name, m=man_year, o=odo_read) '''

if __name__ == "__main__":
    app.run(debug=True)





