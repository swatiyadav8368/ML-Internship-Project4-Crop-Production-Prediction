import joblib
import pandas as pd
from flask import Flask, request, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Load the trained model
model = joblib.load('random_forest_model.joblib')

# Load the preprocessed data to get feature names
df_sample = pd.read_csv('project4_preprocessed_data.csv', nrows=1)
feature_names = df_sample.drop('Production_Quantity', axis=1).columns

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the request
        data = request.get_json(force=True)
        df_input = pd.DataFrame([data])

        # Ensure the input has the same columns as the training data
        df_input_reindexed = df_input.reindex(columns=feature_names, fill_value=0)

        # Make a prediction
        prediction = model.predict(df_input_reindexed)

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction[0]})
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(port=5000)