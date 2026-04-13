import requests

API_URL = "http://127.0.0.1:8000/predict"

print("TEST API")

#1
params_1 = {"message": "I love this application, it is very helpful!"}
response_1 = requests.post(API_URL, params=params_1)
print("\nTest 1 (Câu lịch sự):")
print(response_1.json())

#2
params_2 = {"message": "You are a stupid and toxic idiot!"}
response_2 = requests.post(API_URL, params=params_2)
print("\nTest 2 (Câu độc hại):")
print(response_2.json())