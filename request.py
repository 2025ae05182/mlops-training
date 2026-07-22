import requests
resp = requests.post("http://127.0.0.1:5000/predict",
                     json={"features":[5.1, 3.5, 1.4, 0.2]})
print(resp.json())
