from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model/rf_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=["POST"])

def predict():
    feature_input = [int(x) for x in request.form.values()]
    feature_input[0] = (feature_input[0]-47.61298077)/11.7355363
    print(feature_input[0])
    print(feature_input)
    feature = [np.array(feature_input)]
    y = model.predict(feature)
    if y[0] == 1:
        out = "Yes"
    else:
        out = "No"
    return render_template("index.html", hasil="{}".format(out))

if __name__=="__main__" :
    app.run(debug=True)