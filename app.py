from flask import Flask, request, render_template
from game_of_life import *

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife()
    return render_template('index.html')


@app.route('/live/', methods=['post', 'get'])
def live():
    world = GameOfLife()
    if world.counter > 0:
        world.form_new_generation()
    else:
        world.counter += 1

    return render_template('live.html', world=world, width=20, height=20)
