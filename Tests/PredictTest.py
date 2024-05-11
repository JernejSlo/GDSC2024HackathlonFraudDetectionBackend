from datetime import datetime
from datetime import datetime

import numpy as np
import requests

request = {
    "user_session_id": 1,
    "user_model" : [],
    "transaction_history": [
                        [[2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],],
                        [[2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],
                          [2516,3,74.91,336,4,1.483e+09,0.099198],]
    ],
    "class_names": ["Fraudulent","Not Fraudulent"]
}

response = requests.post('http://localhost:5002/detect_fraud', json=request)

if response.status_code == 200:
    print("Response Content:", response.json())  # Assuming the response is JSON
else:
    print("Failed to retrieve data:", response.text)
