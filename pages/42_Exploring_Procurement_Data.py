import streamlit as st
import pandas as pd
from helper_functions.utility import check_password

st.set_page_config(
    page_title = "Exploring Procurement Data",
    page_icon=":material/shopping_cart:"
)

st.title("Exploring Procurement Data")
st.write(
    "Users can explore different aspects of procurement data from GeBiz from FY2019 to FY2023."
)

# password checkpoint
if not check_password():  
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

    data = data.T.reset_index()
