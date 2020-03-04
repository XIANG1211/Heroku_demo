from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
from keras.models import load_model

app = Flask(__name__)


@app.route('/api', methods=['POST', 'GET'])
def makecalc():
    model=load_model("./models/cnn.h5")
    data = request.get_json("")
    data2=np.array(data)
    prediction =model.predict(data2)
    retrn json.dumps(int(np.argmax(prediction)))
    print(json.dumps(int(np.argmax(prediction))))

if __name__ == '__main__':
    app.run()
