import streamlit as st
from send_email import send_email
import pandas

st. header("contact me")
df = pandas.read_csv("topics.csv")


with st.form(key="my form"):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("what topic do you want to discuss", df)
    row_message = st.text_area("Text")
    message = f"""\
Subject:new email from{user_email}

From: {user_email}
{topic}
{row_message} 
"""
    button = st.form_submit_button("submit")
    if button:
        send_email(message)
        st.info("message send")
