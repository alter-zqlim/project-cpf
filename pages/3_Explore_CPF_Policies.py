import streamlit as st
from helper_functions.utility import check_password

st.set_page_config(
    page_title = "Explore CPF Policies",
    page_icon=":material/group:"
)

st.title("Explore CPF Policies")
st.write(
    "Users can explore different CPF policies through interactive scenarios that illustrate how various policies apply to real-life situations (e.g., housing withdrawals, healthcare financing). This feature will enhance understanding by allowing users to see the practical implications of CPF policies in their lives."
)

# password checkpoint
if not check_password():  
    st.stop()

form = st.form(key = "form")
form.subheader("Prompt")

user_prompt = form.text_area(
    "What queries about CPF policies do you have?", 
    height = 160
)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    print(f"User Input is {user_prompt}")
