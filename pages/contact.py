import streamlit as st

st. header("contact me")

with st.form(key="my form"):
    user_name = st.text_input("Your Email Address")
    row_message = st.text_area("Your Message")
    button = st.form_submit_button("submit")
    if button:
        st.info("message sen")
