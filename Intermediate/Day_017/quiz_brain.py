class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print("The correct answer was: {}".format(current_question.answer))
        print("Your current score is: {}/{}".format(self.score, current_question))

    def still_has_questions(self):
        return not self.question_number == len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input("\nQ.{}: {} (True / False):".format(self.question_number, current_question.question))
        self.check_answer(user_answer, current_question)
