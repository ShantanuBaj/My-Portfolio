import streamlit as st

st.header("Contact me")

with st.form(key="email_form"):
    user_email=st.text_input("Your Email Address")
    message= st.text_area("Your message")
    button= st.form_submit_button("Submit")
    print(button)
    if button:
        print("Pressed")
