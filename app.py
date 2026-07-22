# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 18:34:29 2026

@author: Sourav
"""
import streamlit as st

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="IMT Defender",
    page_icon="🎮",
    layout="centered"
)

# ----------------------------------------------------
# Session Variables
# ----------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"

if "name" not in st.session_state:
    st.session_state.name = ""

if "difficulty" not in st.session_state:
    st.session_state.difficulty = "Easy"

# ----------------------------------------------------
# HOME PAGE
# ----------------------------------------------------
if st.session_state.page == "home":

    st.title("🎮 IMT Defender")

    st.subheader("Information Manipulation Training Game")

    st.write("Welcome to the prototype!")

    st.session_state.name = st.text_input("Enter your Name")

    st.session_state.difficulty = st.radio(
        "Select Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    if st.button("🚀 Start Game"):

        st.session_state.page = "question"

        st.rerun()

# ----------------------------------------------------
# QUESTION PAGE
# ----------------------------------------------------
elif st.session_state.page == "question":

    st.title("Question 1 of 10")

    st.write("### Read the following post")

    st.info("""
Only one study found that Product X is harmful,
while dozens of studies prove it is completely safe.
""")

    answer = st.radio(
        "Which manipulation is used?",
        [
            "Cherry Picking",
            "Fabrication",
            "Exaggeration",
            "Misleading Context"
        ]
    )

    if st.button("Submit"):

        st.session_state.answer = answer

        st.session_state.page = "feedback"

        st.rerun()

# ----------------------------------------------------
# FEEDBACK PAGE
# ----------------------------------------------------
elif st.session_state.page == "feedback":

    st.title("Result")

    if st.session_state.answer == "Cherry Picking":

        st.success("✅ Correct!")

        st.write("""
This is **Cherry Picking** because only one side of the
evidence is presented while contradictory evidence is ignored.
""")

    else:

        st.error("❌ Incorrect")

        st.write("""
Correct answer: **Cherry Picking**
""")

    if st.button("➡ Next Question"):

        st.session_state.page = "question2"

        st.rerun()

# ----------------------------------------------------
# QUESTION 2
# ----------------------------------------------------
elif st.session_state.page == "question2":

    st.title("Question 2 of 10")

    st.info("""
Breaking News!

Scientists have discovered that drinking coffee
will make everyone live 150 years.
""")

    st.radio(
        "Choose the manipulation",
        [
            "Fabrication",
            "Cherry Picking",
            "Misleading Context",
            "Exaggeration"
        ]
    )

    st.button("Submit")
















