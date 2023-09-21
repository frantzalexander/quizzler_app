import requests

parameters = {
    "amount": 10,
    "category": 22,
    "type": "boolean"
}

response = requests.get(
    url = "https://opentdb.com/api.php",
    params = parameters
)

response.raise_for_status()

data = response.json()
quiz_data = data["results"]
print(data)
print(quiz_data)

question_bank = []

for question in quiz_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    