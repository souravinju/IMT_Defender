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
            st.session_state.page = "Scenario1"
            st.rerun()

# ====================================================
# Threat Page
# ====================================================
elif st.session_state.page == "Scenario1":
    st.success(f"Welcome, **{st.session_state.name}**!")
    st.title("🛡️ You will be bombarded with examples of several Manipulated Information 🛡️")

    col1, col2 = st.columns([8, 1])

    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = "Home"
            st.rerun()

    with col2:
        if st.button("Next ➜"):
           st.session_state.page = "Scenario2"
           st.rerun()




# ====================================================
# SCENARIO PAGE 1
# ====================================================
elif st.session_state.page == "Scenario2":

##    st.title("🛡️ You will be bombarded with examples of several Manipulated Information")

##    st.success(f"Welcome, **{st.session_state.name}**!")

    st.write(
        "Before starting the game, learn how to identify"
        "**Exaggerated Truthful Information**. Because The information may be truthful but out of context,but it is deceptive becuase it can be misleading and resembling the product as superior"
    )

    st.divider()

##    st.subheader("Please Check the Advertisement")

    st.markdown("""
<div style="
background:#f8f9fa;
padding:20px;
border-radius:12px;
border:1px solid #dcdcdc;
">

<!-- Layer 1 -->
<h2>📢 Advertisement</h2>

<!-- Layer 2 -->
<p style="font-size:18px;">
👤 <b>Creator:</b> Authorized Company
</p>

<!-- Layer 3 -->
<div style="
background:#FFF8DC;
padding:18px;
border-radius:10px;
border-left:6px solid #FFA500;
">

<h3>🦷 BrightSmile Toothpaste</h3>

<p style="font-size:22px;font-weight:bold;">
80% of dentists recommend BrightSmile toothpaste
</p>

</div>

</div>
""", unsafe_allow_html=True)

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
it manipulates important contextual information such as:

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

    col1, col2 = st.columns([8, 1])

    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = "Home"
            st.rerun()

    with col2:
        if st.button("Next ➜"):
           st.session_state.page = "Scenario3"
           st.rerun()

# ====================================================
# SCENARIO PAGE2
# ====================================================
elif st.session_state.page == "Scenario3":

###    st.title("🛡️ You will be bombarded with examples of several Manipulated Information")

###    st.success(f"Welcome, **{st.session_state.name}**!")

    st.write(
        "Before starting the game, learn how to identify "
        "**Consequential Disinformation**."
    )

    st.divider()

    st.subheader("Please Check the Advertisement")

    st.markdown("""
<div style="
background:#f8f9fa;
padding:20px;
border-radius:12px;
border:1px solid #dcdcdc;
">

<!-- Layer 1 -->
<h2>📢 Advertisement</h2>

<!-- Layer 2 -->
<p style="font-size:18px;">
👤 <b>Creator:</b> Authorized Company
</p>

<!-- Layer 3 -->
<div style="
background:#FFF8DC;
padding:18px;
border-radius:10px;
border-left:6px solid #FFA500;
">

<h3>🦷 Weight loss product</h3>

<p style="font-size:22px;font-weight:bold;">
80% of dentists recommend BrightSmile toothpaste
</p>

</div>

</div>
""", unsafe_allow_html=True)

    st.success(
        """
## ✅ Classification: Consequential Disinformation

This advertisement is an example of
**Consequential Disinformation**.
"""
    )

    st.markdown(
        """
### 🔍 Why is this statement misleading?

Although the statement may be based on a real survey,
it manipulates important contextual information such as:

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
####Next Button 
    col1, col2 = st.columns([8, 1])

    with col1:
        if st.button("⬅ Previous"):
            st.session_state.page = "Home"
            st.rerun()

    with col2:
       if st.button("Next ➜"):
        st.session_state.page = "LaunchGame"
        st.rerun()

if st.session_state.page == "LaunchGame":

    st.title("🎮 Ready to Play?")

    st.write("""
    You have completed the learning section.

    Now you will answer several questions based on
    Information Manipulation Theory.

    Read each advertisement carefully before selecting your answer.

    Good luck!
    """)

    if st.button("Lets Play"):
        st.session_state.page = "Game"
        st.rerun()


# ====================================================
# GAME PAGE
# ====================================================
import streamlit as st
import pandas as pd


def game_page():

    # ---------------------------
    # Read Questions
    # ---------------------------
    questions = pd.read_excel("C:/Users/Sourav/Desktop/IMT_games/IMT.xlsx")

    # ---------------------------
    # Session Variables
    # ---------------------------
    if "question_no" not in st.session_state:
        st.session_state.question_no = 0

    if "score" not in st.session_state:
        st.session_state.score = 0

    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    # ---------------------------
    # Finish Game
    # ---------------------------
    if st.session_state.question_no >= len(questions):

        st.balloons()

        st.title("🎉 Congratulations!")

        st.success("You have completed the IMT Defender Game.")

        accuracy = (st.session_state.score / len(questions)) * 100

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Correct Answers", st.session_state.score)

        with col2:
            st.metric("Accuracy", f"{accuracy:.1f}%")

        st.divider()

        if st.button("🏠 Back to Home"):

            st.session_state.page = "Home"

            st.session_state.question_no = 0
            st.session_state.score = 0
            st.session_state.submitted = False

            st.rerun()

        return

    # ---------------------------
    # Current Question
    # ---------------------------
    q = questions.iloc[st.session_state.question_no]

    st.title("🎮 IMT Defender")

    st.subheader("Can You Identify the Manipulation?")

    st.progress((st.session_state.question_no + 1) / len(questions))

    st.write(
        f"### Question {st.session_state.question_no + 1} of {len(questions)}"
    )

    st.divider()

    # ---------------------------
    # Advertisement
    # ---------------------------

    st.markdown("## 📢 Advertisement")

    st.write(f"**Advertisement Type:** {q['Type']}")

    st.write(f"**Creator:** {q['Creator']}")

    st.info(q["Message"])

    st.divider()

    # ---------------------------
    # Answer Options
    # ---------------------------

    answer = st.radio(
        "Which type of Information Manipulation is this?",
        [
            q["Option1"],
            q["Option2"],
            q["Option3"],
            q["Option4"],
        ],
        key=f"question_{st.session_state.question_no}"
    )

    # ---------------------------
    # Submit
    # ---------------------------

    if not st.session_state.submitted:

        if st.button("Submit Answer"):

            st.session_state.submitted = True

            if answer == q["Correct_Answer"]:

                st.success("✅ Correct!")

                st.session_state.score += 1

            else:

                st.error("❌ Incorrect")

                st.write("### Correct Answer")

                st.success(q["Correct_Answer"])

            st.info(q["Explanation"])

            st.rerun()

    # ---------------------------
    # After Submission
    # ---------------------------

    else:

        if answer == q["Correct_Answer"]:

            st.success("✅ Correct!")

        else:

            st.error("❌ Incorrect")

            st.write("### Correct Answer")

            st.success(q["Correct_Answer"])

        st.info(q["Explanation"])

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Current Score",
                f"{st.session_state.score}/{len(questions)}"
            )

        with col2:

            if st.button("Next Question ➜"):

                st.session_state.question_no += 1
                st.session_state.submitted = False

                st.rerun()

if st.session_state.page == "Game":
    game_page()






