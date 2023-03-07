from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
# p1 = []
# p2 = []
# for item in question_data:
#     for que in item:
#         if que == "text":
#             p1.append(item[que])
#         else:
#             p2.append(item[que])
#
# for i in range(len(p1)):
#     question_bank.append(Question(p1[i], p2[i]))
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text, question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{len(question_bank)}")