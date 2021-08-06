class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
       return len(self.question_list) > self.question_number

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(ans,current_question.answer)
    def check_answer(self,ans,current_question):
        if ans.lower() == current_question.lower():
            self.score += 1
            print("you got it right")
        else:
            print("That's wrong.")
        print(f"The answer is {current_question}")
        print(f"Your current score is {self.score}/{self.question_number} ")
        print("\n")
