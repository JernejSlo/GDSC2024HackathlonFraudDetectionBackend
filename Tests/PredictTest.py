from datetime import datetime
from datetime import datetime

import numpy as np
import requests

request = {
    "user_session_id": 1,
    "user_model" : [
        [30,1,17,342,24,31,186,111,101,178,964,10,16,0,12,642,262,39,23,12,495,435,60,205,497,288,990]
    ],
    "transaction_history": [
                        [[3490,4,77.62,254,1735444860,0,0,1,1,8],
                            [9016,10,77.48,160,1735439903,0,0,1,1,5],
                            [873,1,68.34,247,1735439002,0,0,1,3,8],
                            [7111,8,24.18,272,1735434936,0,0,1,2,8],
                            [275,1,30.26,64,1735430959,0,0,1,3,2],
                            [9651,10,25.16,152,1735430177,0,0,1,3,5],
                            [8423,9,4.42,20,1735430159,0,0,2,2,1],
                            [7895,8,78.22,34,1735429805,0,0,1,2,1],
                            [7672,8,46.49,157,1735429619,0,0,1,1,5],
                            [3363,4,27.99,65,1735429388,0,0,1,1,2]],
    ],
    "class_names": ["Not Fraudulent","Fraudulent"]
}

response = requests.post('http://localhost:5002/detect_fraud', json=request)

if response.status_code == 200:
    print("Response Content:", response.json())  # Assuming the response is JSON
else:
    print("Failed to retrieve data:", response.text)
