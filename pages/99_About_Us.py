import streamlit as st

st.set_page_config(
    page_title = "About Us"
)

st.title("About Us")

st.subheader("This is a detailed page that outlines the project scope, objectives, data sources, and features.")

st.subheader("Data sources")
st.write("Government Procurement via GeBIZ - Dataset of all open tenders put out by government agencies since FY2019. (retrieved on 11 October 2024)")
