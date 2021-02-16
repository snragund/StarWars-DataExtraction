"""Import Modules"""
from flask import Flask, render_template, request,send_file

import pandas as pd
import extract as ex
app = Flask(__name__)

"""Routes"""
@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/names',methods = ['POST','GET'])
def names():
    if 'get_names' in request.form:

        names_list=ex.get_names()
        return render_template('index.html', names_list = names_list)


if __name__ == "__main__":
    
    app.run(debug=True)
