import encodings
from flask import Flask, jsonify, render_template
from flask_cors import CORS, cross_origin
from scraper import *


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/')
def index():
    data = get_headline_midi() + get_headline_lexpress()
    data = sorted(data, key=lambda d: d.date.timestamp(), reverse=True)
    # data = []

    return render_template('index.html', data=data)

@app.route('/api/')
@cross_origin()
def api():
    data = get_headline_midi()
    return jsonify({
        'headlines': {
            'Midi Madagasikara': [d.toJson() for d in data],
            'L\'expresse de Madagascar': [d.toJson() for d in get_headline_lexpress()]
            },

    },  )

if __name__ == "__main__":
    app.run(debug=True)