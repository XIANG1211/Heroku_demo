from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
from PIL import Image
from keras.models import load_model

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(np.argmax(prediction))

if __name__ == '__main__':
    model=load_model("./models/cnn.h5")
    app.run(debug=True)
