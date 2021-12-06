import requests

resp = requests.get(
    "https://addike-tester.herokuapp.com/run-test",
    files={"file": open("solution.py", "r")},  # Change this to your file name
)

print(resp.text)
