'''
Created on 19.03.2019

@author: neumann
'''

import spintax
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def test():
    return "pySpaceBremen TEST"

@app.route("/html")
def html():
    return  spintax.getHtml()

@app.route("/tex")
def tex():
    return  spintax.getText()

@app.route("/spin")
def spin():
    return  spintax.getText() + "<br><br>" + spintax.getHtml()



