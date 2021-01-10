from flask import Flask, request, render_template
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cocopuffers007'
debug = DebugToolbarExtension(app)


@app.route('/')
def create_username():
    return render_template('home.html')


@app.route('/story')
def new_story():
    username = request.args['username']
    return render_template('story.html', username=username)


@app.route('/user-story')
def user_story():
    place = username = request.args['place']
    noun = username = request.args['noun']
    verb = username = request.args['verb']
    adjective = username = request.args['adjective']
    plural_noun = username = request.args['plural_noun']
    return render_template('user_story.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
