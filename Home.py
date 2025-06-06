import streamlit as st
import pandas
import os

current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "stadium1.png")

st.set_page_config(layout="wide")

col1, col2= st.columns(2)


with col1:
    st.image("stadium1.png", width=300)

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

col3, empty_col, col4= st.columns([1.5,0.5,1.5])

df= pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+ row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

