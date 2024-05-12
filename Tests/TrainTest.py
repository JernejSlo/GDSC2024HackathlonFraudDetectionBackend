import requests

window_size = 10
n_classes = 2

request = {
    "model_weights": "./ML/Models/FDMWeights.keras",
    "user_models_path": "./ML/Data/user_models.csv",
    "data_path": "./Tests/transactions.csv",
    "num_classes": 2,
    "user_model": "./ML/Data/user_models.csv",
    "input_shape": (window_size,10),
    "input_shape_user_modeling": (27,),
    "group_by": "UserId",
    "window_size": window_size,
    "target_column": "Fraudulent",
}

response = requests.post('http://localhost:5002/train_model', json=request)

if response.status_code == 200:
    print("Response Content:", response.json())  # Assuming the response is JSON
else:
    print("Failed to retrieve data:", response.text)
    print("Failed to retrieve data:", response.text)