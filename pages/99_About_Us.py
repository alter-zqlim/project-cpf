import streamlit as st

st.set_page_config(
    page_title = "About Us", 
    page_icon = ":material/quiz:"
)

# This is a detailed page that outlines the project scope, objectives, data sources, and features.
st.title("About Us")

st.subheader("Project scope", divider = True)
st.subheader("Objectives", divider = True)
st.subheader("Features", divider = True)

st.subheader("Data sources", divider = True)
st.write("Government Procurement via GeBIZ &mdash; Dataset of all open tenders put out by government agencies since FY2019. (retrieved via data.gov.sg on 11 October 2024)")
st.write("Government Procurement &mdash; https://www.mof.gov.sg/policies/government-procurement (linked on 12 October 2024)")
st.write("Guide to Singapore Procurement &mdash; https://www.gebiz.gov.sg/singapore-government-procurement-regime.html (linked on 12 October 2024) and related documents:")
st.write("-- Government Procurement Guide for Suppliers")
st.write("-- List of Debarment or Disqualification Grounds")
st.write("-- Registration Guidelines for Government Supplier Registration")
st.write("Frequently Asked Questions &mdash; https://www.gebiz.gov.sg/faq.html (linked on 12 October 2024)")
