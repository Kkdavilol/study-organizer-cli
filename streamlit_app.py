import streamlit as st
import requests

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📚 Study Organizer")

st.write("Organize your study tasks and stay motivated.")

# Add task
new_task = st.text_input("New Task")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(
            {"task": new_task, "done": False}
        )

# Show tasks
st.subheader("Your Tasks")

for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])

    with col1:
        status = "✅" if task["done"] else "❌"
        st.write(f"{status} {task['task']}")

    with col2:
        if st.button("Done", key=i):
            st.session_state.tasks[i]["done"] = True

# Motivation API
st.subheader("📖 Motivation")

if st.button("Get Motivation"):
    response = requests.get(
        "https://zenquotes.io/api/random",
        timeout=5
    )

    if response.status_code == 200:
        data = response.json()[0]

        st.success(f'"{data["q"]}"')
        st.write(f'- {data["a"]}')
    else:
        st.error("Could not fetch quote.")
