from flask import Flask, render_template, request,url_for
import pickle
import numpy as np

# setup application
app = Flask(__name__)

with open('model.pkl','rb') as file:
    model=pickle.load(file)
    

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        Open = float(request.form['Open'])
        High = float(request.form['High'])
        Low= float(request.form['Low'])

        data = np.array([[Open,High,Low]])
        pred_value = model.predict(data)
        pred_value = np.round(pred_value[0],2)

    return render_template('index.html', pred_value=pred_value)

# extra code for testing


if __name__ == '__main__':
    app.run(debug=True)
