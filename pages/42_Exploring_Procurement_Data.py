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
    df = pd.read_csv("./data/GovernmentProcurementviaGeBIZ.csv")
    return df.set_index("agency")

df = get_GeBIZ_data()
df_index = df[~df.index.duplicated(keep='first')]

agencies = st.multiselect(
    "Select agencies",
    list(df_index.index),
    ["Competition and Consumer Commission of Singapore (CCCS)"]
)
if not agencies:
    st.error("Please select at least one agency.")
else:
    data = df.loc[agencies]
    st.write("## All procurement projects", data.sort_index())

    data = data.T.reset_index()
    """
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
    )
    chart = (
        alt.Chart(data)
        .mark_area(opacity=0.3)
        .encode(
            x="year:T",
            y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
            color="Region:N",
        )
    )
    st.altair_chart(chart, use_container_width=True)
    """
