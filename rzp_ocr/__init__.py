from flask import Flask


# create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
)

app.config.from_pyfile('config.py')


# a simple page that says hello
@app.route('/hello')
def hello():
    return 'Hello, World!'


import rzp_ocr.analysis
