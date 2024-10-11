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
    df = pd.read_csv(".data/GovernmentProcurementviaGeBIZ.csv")
    return df.set_index("agency")

df = get_GeBIZ_data()
agencies = st.multiselect(
    "Select agencies",
    list(df.index),
    ["Competition and Consumer Commission of Singapore (CCCS)"]
)
if not agencies:
    st.error("Please select at least one agency.")
else:
    data = df.loc[agencies]
    data /= 1000000.0
    st.write("### Gross Agricultural Production ($B)", data.sort_index())
