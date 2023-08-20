from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []
for question in question_data:
    specific_question = Question(question["text"], question["answer"])
    question_bank.append(specific_question)

quizbrain = QuizBrain(question_bank)
while quizbrain.still_has_questions():
    quizbrain.next_question()
print("You've completed the quiz\nYour final score was: {}/{}".format(quizbrain.score, quizbrain.question_number))
