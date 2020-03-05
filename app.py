from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import json
from keras.models import load_model

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1600 * 1024 * 1024

model=load_model("./models/cnn.h5")
@app.route('/api', methods=['POST', 'GET'])
def makecalc():
    data = request.get_json(force=True)
    data=np.array(data["test"])
    #prediction =model.predict(data)
    #return render_template('index.html',title=int(np.argmax(prediction)))
    #return json.dumps(int(np.argmax(prediction)))
    #title = 'Good Flask'
    return render_template('index.html',json=str(data))
if __name__ == '__main__':
    app.run()
