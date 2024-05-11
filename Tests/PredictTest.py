from datetime import datetime
from datetime import datetime

import requests

request = {
    "user_session_id": 1,
    "model_path": "",
    "user_model" : [],
    "transaction_history" : []
}

response = requests.post('http://localhost:5002/detect_fraud', json=request)

if response.status_code == 200:
    print("Response Content:", response.json())  # Assuming the response is JSON
else:
    print("Failed to retrieve data:", response.text)
