from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
from keras.models import load_model

app = Flask(__name__)

model=load_model("./models/cnn.h5")
@app.route('/api', methods=['POST', 'GET'])
def makecalc():
  
    data = request.get_json("",force=True)
    #prediction =model.predict(data)
    #return json.dumps(int(np.argmax(prediction)))
    return str(data)
if __name__ == '__main__':
    app.run()
