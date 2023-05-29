from flask import Flask, render_template, request
import predict
import adaboost_predict
from adaboost import Adaboost

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/classify', methods=['POST'])
def classify():
    sentence = request.form['sentence']
    classifier = request.form['classifier']
    if classifier == 'dt':
        result = predict.classify(sentence)
    elif classifier == 'adaboost':
        result = adaboost_predict.classify(sentence)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
