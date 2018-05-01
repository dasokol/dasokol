from flask import Flask
from flask import render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualizer')
def visualizer():
    return render_template('visualizer.html')

@app.route('/openloop')
def visualizer():
    return render_template('openloop.html')
    
