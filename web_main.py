import streamlit as st
import webapp_functions as wf

todos = wf.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo'] + '\n'
    todos.append(new_todo)
    wf.write_todos(todos)
    st.session_state['new_todo'] = ''


st.title("My Todo App")
st.subheader("Add the tasks you should do..")
st.write("")

for index, todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.pop(index)
        wf.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add a new todo:",
              key='new_todo', on_change=add_todo)
