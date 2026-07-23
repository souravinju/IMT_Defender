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

# -----------------------------
# SCENARIO PAGE
# -----------------------------
elif st.session_state.page == "Scenario":

    st.title("🛡️ Learning Example")

    st.subheader("Advertisement")

    st.info("""
**"80% of dentists recommend BrightSmile toothpaste."**
""")

    st.success("""
## ✅ Classification: Exaggerated Truthful Information

This advertisement is an example of **Exaggerated Truthful Information**.
""")

    st.markdown("""
### 🔍 Why is this statement misleading?

Although the statement may be based on a real survey,
it omits important contextual information such as:

- How many dentists were surveyed?
- Were they independent?
- Was the survey scientifically conducted?
- What exactly were they asked?

Without this context, consumers may believe the product
is superior when the evidence does not necessarily support
that conclusion.

Therefore, this is classified as **Exaggerated Truthful Information**.
""")

    st.warning("""
### 💡 Remember

Always ask:

✔ Where did this information come from?

✔ Is any important context missing?

✔ Does the evidence justify the claim?
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
















