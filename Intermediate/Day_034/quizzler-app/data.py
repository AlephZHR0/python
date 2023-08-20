import requests
NUMBER_OF_QUESTIONS = 10
parameters = {
    "amount":NUMBER_OF_QUESTIONS,
    "type":"boolean"
}

request = requests.get(url="https://opentdb.com/api.php", params=parameters)
questions = request.json()["results"]
question_data = []
for i in range(NUMBER_OF_QUESTIONS):
    question_data.append({
        "category": questions[i]["category"],
        "type": questions[i]["type"],
        "difficulty": questions[i]["difficulty"],
        "question": questions[i]["question"],
        "correct_answer": questions[i]["correct_answer"],
        "incorrect_answers": [questions[i]["incorrect_answers"]]
    })