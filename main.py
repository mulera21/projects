import streamlit as st
import pandas

st.set_page_config(layout="wide")
st.subheader("The Best Company")


nice = (""" i have done programming courses  in udemy to increase my skills in
    programming and at per now am focusing on,
    enrolling AWS course. The skills i have encompass writing Python code,
    debugging programs, and solving problems using Python scripts.also familiar with 
    popular Python libraries and frameworks such as streamlit,django and flask.
    """)
st.write(nice)

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data.csv")


with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(f'{row["role"].title()}')
        st.image("images/" + row["image"])


with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(f'{row["role"].title()}')
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.subheader(f'{row["role"].title()}')
        st.image("images/" + row["image"])






