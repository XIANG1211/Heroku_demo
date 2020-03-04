from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json
from keras.models import load_model

app = Flask(__name__)

model=load_model("./models/cnn.h5")
@app.route('/api', methods=['POST', 'GET'])
def makecalc():
  
    data = request.get_json()
    data2=np.array(data[""])
    #prediction =model.predict(data2)
    #return json.dumps(int(np.argmax(prediction)))
    return str(data2.shape)
if __name__ == '__main__':
    app.run()
