

from flask import Flask,render_template,request,jsonify
import joblib
import pandas as pd
import pickle




app=Flask(__name__)

#load the pickle model
rf_clf=pickle.load(open("model.pkl","rb"))


@app.route('/', methods=['GET'])
def hello_world():
     return render_template('home.html')

@app.route("/sub", methods = ["POST"])
def submit():
    # Html to py
    if request.method == "POST":
        name = request.form["Username"]
        return render_template("sub.html", n=name)


@app.route('/predict', methods=['POST'])

def main():


def predict():
    prediction = rf_clf.predict()
    test_image = im.resize((150, 150))
    return render_template("index.html",prediction= rf_clf.predict)


if __name__ =="__main__":
    app.run(port=5000,debug=True)

