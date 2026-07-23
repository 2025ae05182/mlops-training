import requests

payload = {
    "Make": "Toyota",
    "Model": "Camry",
    "Year": 2022,
    "Fuel_Type": "Petrol",
    "Transmission": "Automatic",
    "Engine_Size": 1.9,
    "Mileage": 32813,
    "Horsepower": 149.0,
    "Torque": 141.0,
    "Owners": 1,
    "Accident_History": 0.0,
    "Service_History": "Full Service",
    "Color": "Brown",
    "Body_Type": "Sedan",
    "Drivetrain": "FWD",
    "Fuel_Efficiency": 38.0,
    "Location": "CA"
}

resp = requests.post("http://127.0.0.1:8000/predict", json=payload)
print(resp.status_code)
print(resp.json())
