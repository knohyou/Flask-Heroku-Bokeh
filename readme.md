# Demonstration of a standalone bokeh document into a simple Flask application deployed on Heroku 

## Basic Overview
These instructions will get you a copy of the project up and running on your local machine. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
* Setup a free Heroku account
* Login heroku account ``` heroku login ``` 
* Python 
 
## Run initial test 
Copy the project into local machine using ```git clone```
```
$ python app.py
```
Test code on local machine by visiting http://localhost:5000

## First time Deploying on Heroku
```
$ heroku create 
$ git add .
$ git commit -m "Commit" 
$ git push heroku master
$ heroku ps:scale web=1
$ heroku open
```

## Running the app locally through heroku
If using Windows, run code below 
```
$ heroku local web -f Procfile.windows 
```
Open http://localhost:5000 in browser to see app running locally


## Acknowledgments
Here are some additional resources and tutorials to follow 
https://github.com/bev-a-tron/MyFlaskTutorial
Bokeh code pulled from 
https://github.com/bokeh/bokeh/tree/master/examples/embed/simple


