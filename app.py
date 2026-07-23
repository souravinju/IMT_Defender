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
    st.session_state.page = "Home"

if "name" not in st.session_state:
    st.session_state.name = ""

if "consent" not in st.session_state:
    st.session_state.consent = "Yes"

# ====================================================
# HOME PAGE
# ====================================================
if st.session_state.page == "Home":

    st.title("🎮 IMT Defender")
    st.header("Information Manipulation Training Game")

    st.write("Welcome to the prototype!")

    name = st.text_input(
        "Enter your Name",
        value=st.session_state.name
    )

    consent = st.radio(
        "I want to play this game",
        ["Yes", "No"],
        index=0 if st.session_state.consent == "Yes" else 1
    )

    if st.button("Start Game"):

        if name.strip() == "":
            st.warning("Please enter your name.")
        elif consent == "No":
            st.warning("You must agree to play the game.")
        else:
            st.session_state.name = name
            st.session_state.consent = consent
            st.session_state.page = "Scenario"
            st.rerun()

# ====================================================
# SCENARIO PAGE
# ====================================================
elif st.session_state.page == "Scenario":

    st.title("🛡️ You will be bombarded with examples of several Manipulated Information")

    st.success(f"Welcome, **{st.session_state.name}**!")

    st.write(
        "Before starting the game, learn how to identify "
        "**Exaggerated Truthful Information**. Because The information may be truthful but out of context that incite misleading to consumer"
    )

    st.divider()

    st.subheader("Advertisement")

    st.info(
        """
### Advertisement

**"80% of dentists recommend BrightSmile toothpaste."**
"""
    )

    st.success(
        """
## ✅ Classification: Exaggerated Truthful Information

This advertisement is an example of
**Exaggerated Truthful Information**.
"""
    )

    st.markdown(
        """
### 🔍 Why is this statement misleading?

Although the statement may be based on a real survey,
it omits important contextual information such as:

- How many dentists were surveyed?
- Were they independent?
- Was the survey scientifically conducted?
- What exactly were they asked?
- Was the survey sponsored by the manufacturer?

Without this information, consumers may incorrectly conclude
that the toothpaste is objectively superior.

The claim appears truthful, but it exaggerates the strength of
the evidence by omitting important context.

Therefore, according to the Information Manipulation Theory (IMT),
this message is classified as:

## **Exaggerated Truthful Information**
"""
    )

    st.warning(
        """
### 💡 What should you learn?

Whenever you encounter statements such as:

- "90% of experts recommend..."
- "Clinically proven..."
- "Most doctors recommend..."
- "Number 1 recommended brand..."

Ask yourself:

✔ Where did this information come from?

✔ Is important context missing?

✔ Does the evidence really justify the claim?

These questions will help you recognize
**Exaggerated Truthful Information**
and become more resistant to information manipulation.
"""
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = "Home"
            st.rerun()

    with col2:
        if st.button("Next ➜"):
            st.session_state.page = "Question1"
            st.rerun()

# ====================================================
# QUESTION 1
# ====================================================
elif st.session_state.page == "Question1":

    st.title("Question 1")

    st.success(f"Participant: **{st.session_state.name}**")

    st.write(
        "Read the following advertisement and identify the type of information manipulation."
    )

    st.info(
        """
**Advertisement**

"Thousands of customers have switched to our bank because it offers the best interest rates."
"""
    )

    answer = st.radio(
        "Which manipulation technique is used?",
        [
            "Exaggerated Truthful Information",
            "Cherry Picking",
            "Partial Information",
            "Fabricated Information",
            "Inconclusive Information",
        ]
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous", key="back_q1"):
            st.session_state.page = "Scenario"
            st.rerun()

    with col2:
        if st.button("Submit"):
            st.success(f"You selected: **{answer}**")
















