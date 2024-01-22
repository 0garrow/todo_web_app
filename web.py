import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(
    page_title="Todo Web App",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"About": "My GitHub: https://github.com/0garrow"},
)


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write(
    "This app is to increase your <u><b>productivity</b></u>.", unsafe_allow_html=True
)

st.text_input(
    label="Enter todo",
    label_visibility="hidden",
    placeholder="Enter a todo.",
    on_change=add_todo,
    key="new_todo",
)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()
