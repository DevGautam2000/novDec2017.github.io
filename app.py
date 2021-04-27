
from flask import Flask, jsonify
import json
app = Flask(__name__)


f = open('./json/17.nov_dec_2017.json')
novDec2017 = json.load(f)
f.close()


@app.route('/novDec2017', methods=['GET'])
def get():
    return jsonify(
        {'nov_dec_2017': novDec2017}
    )


if __name__ == "__main__":
    app.run(debug=True)
