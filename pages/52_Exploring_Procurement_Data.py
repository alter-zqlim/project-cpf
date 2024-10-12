import streamlit as st
import pandas as pd
from helper_functions import utility
from helper_functions import llm

st.set_page_config(
    page_title = "Exploring Procurement Data",
    page_icon=":material/shopping_cart:"
)

st.title("Exploring Procurement Data")
st.write(
    "Users can explore procurement data from GeBiz, based on various procuring agencies, from FY2019 to FY2023."
)

# password checkpoint
if not utility.check_password():  
    st.stop()

@st.cache_data
def get_GeBIZ_data():
    unsorted_df = pd.read_csv("./data/GovernmentProcurementviaGeBIZ.csv")
    return unsorted_df.set_index("agency")

unsorted_df = get_GeBIZ_data()
df = unsorted_df.sort_values(by = ['agency', 'tender_no', 'supplier_name', 'award_date'])
df_index = df[~df.index.duplicated(keep = 'first')]

agencies = st.multiselect(
    "Select agencies",
    list(df_index.index),
    ["Competition and Consumer Commission of Singapore (CCCS)"]
)
if not agencies:
    st.error("Please select at least one agency.")
else:
    data = df.loc[agencies]
    st.write("## Procurement projects", data.sort_index())


def process_user_message(user_input):
    delimiter = "```"
    answer = ""
    # check_for_malicious_intent
    if llm.check_for_malicious_intent(user_input) == 'Y':
        answer = "We are unable to process your request. Please rephrase your query or try a different query."
    else:
        answer = "Thank you for your query!"
    return answer

form = st.form(key = "form")
form.subheader("What would you like to know about the above GeBiz procurement data from FY2019 to FY2023?")

user_prompt = form.text_area(
    "Please enter your query below", 
    height = 160
)

if form.form_submit_button("Submit"):
    st.toast(f"User Input Submitted - {user_prompt}")
    response = llm.get_completion(user_prompt)
    st.write(response)
