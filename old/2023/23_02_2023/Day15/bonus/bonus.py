import json
with open("ques.json",'r') as file:
    content = file.read()

score=0
data =json.loads(content)
for qn,que in enumerate(data):
    print(que["question_text"])
    for index,alter in enumerate(que["alternative"]):
        print(index+1,".",alter)
    user_input = int(input("Enter your answer: "))
    que["user_input"]=user_input
    if que["user_input"]==que["correct_ans"]:
        score =score+1
        result ="correct answer"
        print(result)
    else:
        print("Wrong Answer")
    message = f"{result} Q.{qn + 1} Your answer : {que['user_input']}," \
              f"Correct answer: {que['correct_ans']}"
    print(message)


print(score,"/",len(data))





