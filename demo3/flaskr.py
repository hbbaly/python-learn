# -*- coding: utf-8 -*-
from db import Test

from flask import Flask, render_template

app = Flask(__name__)
test = Test()
@app.route('/hello/')
def hello():
    # user = test.query_all()
    # print(user)
    name = 'body'
    return render_template('list.html', name=name)
if __name__ == '__main__':
    app.run(debug=True)