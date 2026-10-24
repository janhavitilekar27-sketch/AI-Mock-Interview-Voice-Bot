import streamlit as st

st.title("🤖 AI Mock Interview Bot")

name = st.text_input("Enter your name")

interview = st.selectbox(
    "Choose Interview Type",
    ["Python", "Machine Learning", "Data Science", "HR Interview"]
)

if st.button("🚀 Start Interview"):
    st.success("Interview Started!")

    st.write("Welcome", name)
    st.write("Your interview type:", interview)

    st.subheader("Question 1")
    st.write("What is Python?")