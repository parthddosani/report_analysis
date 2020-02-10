from flask import Flask, request, redirect, url_for, flash, jsonify
from flask_cors import CORS
import numpy as np
import pickle as p
import json


app = Flask(__name__)
CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'
# CORS(app, resources={r"/api": {"origins": "*"}})

@app.route('/api', methods=['POST'])
# @crossdomain(origin="*", headers=["Content-Type"])
def makecalc():


    data=request.get_json()
    print(data)
    # data1 = json.dumps(data1)
    # data = request.get_data()
    print(data)
    data = data['data']
    data = data.split(',')
    final_list = []
    for r in data:
        final_list.append(float(r))
    print(type(data))
    print("parth")
    data1 = []
    data1.append(list(final_list))
    print(data1)

    modelfile = 'prediction.pickle'
    model = p.load(open(modelfile, 'rb'))
    
    b = model.predict(data1)
    c = model.predict_proba(data1)
    print(type(b))
    print(b)
    print(type(c))
    print(c)

    prediction = np.array2string(b)
    print(prediction)
    
    prediction = np.array2string(c[0])
    prediction = prediction[1:-1]
    prediction = prediction.split(" ")
    a = float(prediction[1])
    a = a * 100
    prediction = str(a)
    print(prediction)
    #prediction.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(prediction)
    #return jsonify(prediction[1])
    
    # return jsonify("parth")

if __name__ == '__main__':
    app.run(debug=True)
