import streamlit as st
from send_email import  send_email

st. header("contact me")

with st.form(key="my form"):
    user_email = st.text_input("Your Email Address")
    row_message = st.text_area("Your Message")
    message = f"""\
Subject:new email from{user_email}

From: {user_email}
{row_message} 
"""
    button = st.form_submit_button("submit")
    if button:
        send_email(message)
        st.info("message send")
