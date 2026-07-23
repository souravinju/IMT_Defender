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
# -----------------------------
# HOME PAGE
# -----------------------------
if st.session_state.page == "Home":

    st.title("🎮 IMT Defender")
    st.header("Information Manipulation Training Game")

    name = st.text_input("Enter your Name")

    consent = st.radio(
        "I want to play this game",
        ["Yes", "No"]
    )

    if st.button("Start Game"):

        if name.strip() == "":
            st.warning("Please enter your name.")
        else:
            st.session_state.name = name
            st.session_state.consent = consent
            st.session_state.page = "Scenario"
            st.rerun()

# -----------------------------
# SCENARIO PAGE
# -----------------------------
# -----------------------------
# SCENARIO PAGE
# -----------------------------
elif st.session_state.page == "Scenario":

    # Get name entered on first page
    participant = st.session_state.get("name", "Participant")

    st.title("🛡️ IMT Learning Module")

    st.success(f"Welcome, **{participant}**! 👋")

    st.write("""
Before you begin the game, you will learn how to identify
different types of information manipulation.
    """)

    st.divider()

    st.subheader("Example Advertisement")

    st.info("""
**"80% of dentists recommend BrightSmile toothpaste."**
""")

    st.success("""
### ✅ Classification: Exaggerated Truthful Information

This advertisement is classified as **Exaggerated Truthful Information**.
""")

    st.markdown("""
### 🔍 Why is this statement misleading?

Although the claim may be factually correct, it exaggerates the
strength of the evidence by omitting important context.

For example, it does not explain:

- How many dentists were surveyed.
- Whether they were independent.
- Whether the survey was scientifically conducted.
- Whether they compared all toothpaste brands.

Consumers may therefore conclude that the toothpaste is objectively
superior even though the evidence may not justify that conclusion.
""")

    st.warning("""
### 💡 What should you learn?

Whenever you encounter claims such as:

- "90% of experts recommend..."
- "Clinically proven..."
- "Most doctors agree..."

Ask yourself:

✔ What evidence supports the claim?

✔ Is important context missing?

✔ Does the evidence justify the conclusion?

These questions will help you recognize **Exaggerated Truthful Information**.
""")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = "Home"
            st.rerun()

    with col2:
        if st.button("Next ➜"):
            st.session_state.page = "Question1"
            st.rerun()
















