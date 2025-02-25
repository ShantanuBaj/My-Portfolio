import streamlit as st

st.set_page_config(layout="wide")

col1, col2= st.columns(2)

with col1:
    st.image("stadium1.png")

with col2:
    st.title("Shantanu Bajpai")
    content= """Dedicated and results-driven professional with extensive experience in IP Service Operations and HR processes. Proven ability to
manage complex data, optimize processes, and ensure high-quality client and employee support. Adept at collaborating with
cross-functional teams to drive data-driven decision-making and process improvements."""
    st.info(content)

content2= """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)
