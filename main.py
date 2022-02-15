from flask import Flask,render_template
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

app=Flask('firtapp')
@app.route('/')
def printhello():
    return 'hello1'

if __name__=='__main__':
    port=8080
    app.run(port=port,debug=True)
