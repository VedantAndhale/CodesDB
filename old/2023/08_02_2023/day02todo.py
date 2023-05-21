"""
user_prompt = 'Enter a Todo :'
todos = []
while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    print(todo.title())
    todos.append(todo)
    print(todos)
"""
# experiment 1 : infinite while-loop - how long will it run ? speed of your processor
# experiment 2 : inside vs outside loop - keep inside only things which need repetition
# experiment 3 : use capitalize vs title - only 1st letter and in title all word first letter
# experiment 4 : no print, no output. no parentheis, no output eg titlt instead of title().
# != : means not equal bonus
x=1
while x<=6:
    print(x)
    x = x + 1