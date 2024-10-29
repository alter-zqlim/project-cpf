import streamlit as st

st.set_page_config(
    page_title = "About Us", 
    page_icon = ":material/quiz:"
)

# This is a detailed page that outlines the project scope, objectives, data sources, and features.
st.title("About Us")

st.subheader("Project scope", divider = True)
st.write("A prototype interface for businesses to navigate government procurement, its rules, as well as better understand historical information on tenders awarded via GeBiz.")
st.write(" ")
st.subheader("Objectives", divider = True)
st.write("Help businesses answer queries on government procurement as well as navigate and query historical procurement data. Showcase use of large language models, retrieval augmented generation as well as agents and tasks, including application of LangChain modules.")
st.write(" ")
st.subheader("Features", divider = True)
st.write("There are 2 apps available. One is purely a query interface where users can type in queries on government procurement. Sample queries have been provided to aid the user in formulating their questions. The second app allows users to filter historical government procurement data and apply queries to it.")
st.write(" ")
st.subheader("Data sources", divider = True)
st.write("Government Procurement via GeBIZ &mdash; Dataset of all open tenders put out by government agencies since FY2019. (retrieved via data.gov.sg on 11 October 2024)")
# st.write("Government Procurement &mdash; https://www.mof.gov.sg/policies/government-procurement (linked on 12 October 2024)")
st.write("Documents found on Guide to Singapore Procurement &mdash; https://www.gebiz.gov.sg/singapore-government-procurement-regime.html (linked on 12 October 2024):")
st.markdown(
    """
    - Government Procurement Guide for Suppliers
    - List of Debarment or Disqualification Grounds
    - Registration Guidelines for Government Supplier Registration
    """
)
st.write(" ")
st.image("./assets/beach.jpg")
# st.write("Frequently Asked Questions &mdash; https://www.gebiz.gov.sg/faq.html (linked on 12 October 2024)")
