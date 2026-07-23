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
        "I want to play that game",
        ["Yes", "No"]
    )

    if st.button("Start Game"):

        st.session_state.page = "Scenario"

        st.rerun()

# ----------------------------------------------------
# QUESTION PAGE
# ----------------------------------------------------
# ----------------------------------------------------
# SCENARIO PAGE
# ----------------------------------------------------
elif st.session_state.page == "Scenario":

    st.title("🛡️ Learn to Detect Information Manipulation")

    st.warning("""
### ⚠️ Threat

In everyday life, advertisements, social media posts, and online reviews often contain
manipulated information that can influence your decisions without you realizing it.
During this training, you will learn how to recognize these manipulation techniques
and become more resistant to them.
""")

    st.divider()

st.subheader("Example")

st.info("""
### Advertisement

**"80% of dentists recommend BrightSmile toothpaste."**
""")

st.success("""
## ✅ Classification: Exaggerated Truthful Information

This advertisement is an example of **Exaggerated Truthful Information**.

The claim may be **factually true**, but it exaggerates its persuasive impact by
omitting important contextual information that consumers need to properly evaluate
the message.
""")

st.markdown("""
### 🔍 Why is this statement misleading?

Although the statement may be based on a real survey, it does **not provide enough
information** for consumers to judge whether the claim is meaningful.

Important information is missing, such as:

- How many dentists participated in the survey?
- Were the dentists independent or sponsored by the company?
- Were they asked to recommend **this toothpaste over all competitors**, or simply whether they would recommend it?
- Was the survey scientifically designed and representative?

Because these details are omitted, consumers may incorrectly conclude that the
toothpaste is objectively superior. The advertisement therefore **exaggerates the
strength of the evidence while remaining factually plausible**, making it an example
of **Exaggerated Truthful Information**.
""")

st.warning("""
### 💡 What should you learn?

When you encounter persuasive claims such as **"most doctors recommend,"**
**"clinically proven,"** or **"90% of experts agree,"** always ask:

✔ What evidence supports this claim?  
✔ Is important context missing?  
✔ Does the evidence really justify the conclusion?

By asking these questions, you can better recognize **Exaggerated Truthful Information**
and become more resistant to information manipulation.
""")

if st.button("Next ➜"):
    st.session_state.page = "Question1"
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
















