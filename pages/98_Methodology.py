import streamlit as st

st.set_page_config(
    page_title = "Methodology", 
    page_icon = ":material/assistant_navigation:"
)

st.title("Methodology")

st.subheader("A comprehensive explanation of the data flows and implementation details.")
st.subheader("A flowchart illustrating the process flow for each of the use cases in the application.")
st.subheader("For example, if the application has two main use cases: a) chat with information and b) intelligent search, each of these use cases should have its own flowchart.")
st.subheader("Links to an external site. for the samples of the flowcharts and methodology (Slide 13, 14, and 15).")

st.image(
    "./assets/street.jpg",
    caption = "Watercolour ink image of a flooded post-apocalyptic street lined with abandoned shophouses of varying heights and sizes. The sky is cloudy and rust red."
)

st.subheader("General Guide to Government Procurement")
st.image(
    "./assets/flow_02.jpg",
    caption = "Answers user queries based on pre-loaded set of 3 PDF documents. Pre-retrieval is improved through semantic chunking. Post-retrieval process is improved through filtering by score threshold. Query is also checked for relevance to the pre-loaded subject matter loaded."
)

