from flask import Flask, request, render_template
from stories import story
app = Flask(__name__)

@app.route('/')
def home():

    prompts = story.prompts

    return render_template('home.html', prompts=prompts)

@app.route('/story')
def display_story():

    text = story.generate(request.args)

    return render_template('story.html', text=text)
