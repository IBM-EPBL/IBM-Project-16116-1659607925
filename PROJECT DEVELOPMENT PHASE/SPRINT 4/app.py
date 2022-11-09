from flask import Flask , request ,url_for , render_template
import numpy as np
import pickle


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

if __name__ =='__main__':
    app.run(debug=True)
