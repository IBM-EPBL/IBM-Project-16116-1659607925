from flask import Flask , request, jsonify, render_template
import numpy as np
import pickle
import requests

API_KEY = 'ufnwpckqlgq5v2Z7NTeWXVb6uqr8xo4zfk_RPXKP9v68'
token_response = requests.post('https://iam.cloud.ibm.com/identity/token',data={"apikey": 
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

sc = pickle.load(open('sc.pkl' , 'rb'))

model = pickle.load(open('model.pkl' , 'rb'))
app = Flask(__name__)


@app.route('/')
def home():
    
    return render_template('index.html')




@app.route('/predict' , methods=['POST'])
def predict():
    inputs = [float(x) for x in request.form.values()]
    inputs = np.array([inputs])
    inputs = sc.transform(inputs)
    output = model.predict(inputs)
    if output < 0.5:
        output = 0
    else:
        output = 1
    return render_template('result.html' , prediction = output)



response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/d5fddf3d-a99d-4409-b576-e5f2b11f904c/predictions?version=2022-11-18',  headers={'Authorization': 'Bearer ' + mltoken})

if __name__ =='__main__':
    app.run(debug=True)
