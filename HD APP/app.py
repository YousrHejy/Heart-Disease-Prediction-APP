import numpy as np
import pickle
from flask import Flask, request, render_template



# Create application
app = Flask(__name__)


# # Load machine learning model
# model = pickle.load(open(‘model.pkl’, ‘rb’))


# Bind home function to URL
@app.route('/')
def home():
    return render_template('page.html')



# # Bind predict function to URL
# @app.route('/predict', methods =['POST'])
# def predict():
 
#     # Put all form entries values in a list 
#     features = [float(i) for i in request.form.values()]
#     # Convert features to array
#     array_features = [np.array(features)]
#     # Predict features
#     prediction = model.predict(array_features)
 
#     output = prediction
 
#     # Check the output values and retrieve the result with html tag based on the value
#  if output == 1:
#     return render_template('Heart Disease Classifier.html', 
#  result = 'The patient is not likely to have heart disease!')
#  else:
#     return render_template('Heart Disease Classifier.html', 
#  result = 'The patient is likely to have heart disease!')


if __name__ == '__main__':
   app.run(debug=True)