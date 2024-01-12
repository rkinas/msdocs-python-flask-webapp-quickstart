import os

# from flask import (Flask, redirect, render_template, request,
#                    send_from_directory, url_for)

# app = Flask(__name__)


# @app.route('/')
# def index():
#    print('Request for index page received')
#    return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# @app.route('/hello', methods=['POST'])
# def hello():
#    name = request.form.get('name')

#    if name:
#        print('Request for hello page received with name=%s' % name)
#        return render_template('hello.html', name = name)
#    else:
#        print('Request for hello page received with no name or blank name -- redirecting')
#        return redirect(url_for('index'))


# if __name__ == '__main__':
#    app.run()

from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/get_weekday', methods=['GET'])
def get_weekday():
    date_str = request.args.get('date', default = '', type = str)
    try:
        date_obj = datetime.strptime(date_str, '%d.%m.%Y')
        return jsonify({'weekday': date_obj.strftime('%A')})
    except ValueError:
        return jsonify({'error': 'Invalid date format. Please use DD.MM.YYYY'}), 400
    
@app.route('/get_multi', methods=['GET'])
def get_weekday():
    number = request.args.get('number', default = '', type = int)
    try:
        date_obj = number * number
        return jsonify({'multi': date_obj})
    except ValueError:
        return jsonify({'error': 'Invalid number format. Please use 5 or 6 etc.'}), 400

if __name__ == '__main__':
    app.run()