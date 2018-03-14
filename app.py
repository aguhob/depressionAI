from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import time
import pickle

app = Flask(__name__)
app.vars = {}

model = pickle.load(open('hrvql209f.pkl', 'rb'))

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('/index.html')

    else:
        val1 = request.form['hr']
        X = np.array([[int(val1)]])
        result = model.predict(X.astype(int))
#print result using {{}} and in render template below
        if result <= .535:
            return render_template('page3.html')
        return render_template('page4.html') #insert result here  

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)
    
