import requests

window_size = 5
n_classes = 2

request = {
    "model_weights": "./ML/Models/FDMWeights.keras",
    "user_models_path": "./ML/Data/user_models.csv",
    "data_path": "./ML/Data/test_data.csv",
    "num_classes": 2,
    "user_model": "./ML/Data/user_models.csv",
    "input_shape": (n_classes,7),
    "group_by": "user_id",
    "window_size": window_size,
    "target_column": "time_since_last_here",
}

response = requests.post('http://localhost:5002/train_model', json=request)

if response.status_code == 200:
    print("Response Content:", response.json())  # Assuming the response is JSON
else:
    print("Failed to retrieve data:", response.text)
    print("Failed to retrieve data:", response.text)