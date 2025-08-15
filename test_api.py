import requests
import json

# Define the API endpoint URL
url = 'http://127.0.0.1:5000/predict'

# Create sample input data that your model expects
# You'll need to fill this with sample data from your preprocessed data file
sample_data = {
    "Year": 2010.0,
    "Crop_Index": 1.5,
    "Production_Value": 5000.0,
    "Area_Value": 250.0,
    "Yield_Value": 20.0,
    "Cost of Cultivation (`/Hectare) A2+FL": 1500.0,
    "Cost of Cultivation (`/Hectare) C2": 2500.0,
    "Cost of Production (`/Quintal) C2": 150.0,
    "Yield (Quintal/ Hectare) ": 18.0,
    # Add your one-hot encoded columns here with a value of 0 or 1
    # You'll need to get these column names from your df_encoded dataframe
    # For example:
    # "Crop_Paddy": 1,
    # "State_Uttar Pradesh": 1,
    # and so on for all your categorical features
}

# Send a POST request to the API
response = requests.post(url, json=sample_data)

# Print the response from the API
if response.status_code == 200:
    print("API Response:", response.json())
else:
    print("Error:", response.status_code, response.text)