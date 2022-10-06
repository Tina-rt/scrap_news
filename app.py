import encodings
from flask import Flask, jsonify
from scraper import *


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route('/')
def index():
    data = get_headline_midi()
    return jsonify({
        'headlines': {
            'midimadagasikara': [d.toJson() for d in data],
            'lexpress': [d.toJson() for d in get_headline_lexpress()]
            },

    },  )

# if __name__ == "__main__":
#     app.run(debug=True)