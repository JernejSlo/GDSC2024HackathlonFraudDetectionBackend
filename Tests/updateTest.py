import requests

request = {
    "transaction": [725,8,18.26,237,1451861703,0,0.0,0,"Travel","Other","Physical"]
}
response = requests.post('http://localhost:5002/update_user_model', json=request)

if response.status_code == 200:
    print("Response Content:", response.json())  # Assuming the response is JSON
else:
    print("Failed to retrieve data:", response.text)

