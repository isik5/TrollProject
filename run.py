import json
from flask import (Flask, request, abort)
from src.evaluator import Evaluator

app = Flask('troll_tespit',
            template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        screen_name = request.form['screen_name']
        evaluator = Evaluator(app.root_path)
        status, result = evaluator.evaluate(screen_name)
        if status != 200:
            return abort(status, result)
        return json.dumps(result)
    else:
        return False

if __name__ == '__main__':
    app.run()