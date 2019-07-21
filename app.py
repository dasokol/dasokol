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
def openloop():
    return render_template('openloop.html')

@app.route('/ai_text_generator')
def ai_text_generator():
    return render_template('ai_text_generator.html')

@app.route('/ai_art_generator')
def ai_art_generator():
    return render_template('ai_art_generator.html')
