# An Exercise Using Flask web framework deployed on Heroku to implement a simple 


## Basic Overview

## Introduction
Need to setup a free Heroku account
Follow tutorial from Heroku with Python https://devcenter.heroku.com/articles/getting-started-with-python#introduction

Python 

# Create a simple flask app

'''
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
   app.run(debug=True, use_reloader=True)
'''
Test code on local machine by visiting http://localhost:5000
$ python app.py

# 

## First time Deploying on Heroku
$ heroku create 
$ git add .
$ git commit -m "Commit" 
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open

## Running the app locally through heroku
If using Windows
$ heroku local web -f Procfile.windows 
Open http://localhost:5000 in browser to see app running locally


