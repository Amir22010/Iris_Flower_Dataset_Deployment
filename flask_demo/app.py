#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pickle

app = Flask(__name__)
Bootstrap(app)
#######################################################################################
#
# Functions
#
#######################################################################################
def iris_model(data):
    filename = "pickle_model2.pkl"
    clf = pickle.load(open(filename, 'rb'))
    my_prediction = clf.predict([data])
    return my_prediction




@app.route('/', methods = ['GET','POST'])
def index2():

    if request.method == 'GET':
        return render_template('index2.html')

    if request.method == 'POST':
        namequery1 = request.form['sepal_length']
        namequery2 = request.form['sepal_width']
        namequery3 = request.form['petal_length']
        namequery4 = request.form['petal_width']
        data = [float(namequery1), float(namequery2), float(namequery3), float(namequery4)]
        flower_pred = int(iris_model(data)[0])
        return render_template('index2.html', prediction=str(flower_pred))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)








