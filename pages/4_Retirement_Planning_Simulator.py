import streamlit as st
from helper_functions.utility import check_password

st.set_page_config(
    page_title = "Retirement Planning Simulator",
    page_icon=":material/group:"
)

st.title("Retirement Planning Simulator")
st.write(
    "This use case will allow users to simulate various retirement scenarios based on information, such as their retirement goals, current CPF savings, expected contributions, and retirement age. Users can adjust parameters to see how different financial choices affect their retirement funds, helping them make informed decisions about their financial future, housing decision, based on accurate and latest information about CPF policy."
)

# password checkpoint
if not check_password():  
    st.stop()
