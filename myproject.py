from flask import Flask
myproject = Flask(__name__)

@myproject.route('/')
def hello_world_lulu():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    return 'Hello World!'

if __name__ == '__main__':
    myproject.run(debug=True)