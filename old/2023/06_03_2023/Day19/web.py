import streamlit
import streamlit as web
import functions
todos = functions.get_todos()

def add_todo():
    todo = web.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

web.title("My Todo App")
web.subheader("This my personal todo app.")
web.write("This app is to increase yout <b>productivity</b>",
          unsafe_allow_html=True)

for index,todo in enumerate(todos):
    checkbox = web.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del streamlit.session_state[todo]
        streamlit.experimental_rerun()

web.text_input(label="Enter New Todo",placeholder="add new todo...",
               on_change=add_todo,key='new_todo')

# code exp 1: layout work according to its order from top to bottom
# code exp 2: can use custom html in string
# code exp 3: st.set_page_config(layout="wide")  to change the page fitting
# code exp 4: you can also creat custome pages