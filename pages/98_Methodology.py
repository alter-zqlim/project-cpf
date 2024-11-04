import streamlit as st

st.set_page_config(
    page_title = "Methodology", 
    page_icon = ":material/assistant_navigation:"
)

st.title("Methodology")

st.subheader("I. Guide to Government Procurement")
st.markdown(
    """
    This app assists the user in their queries on government procurement in general.
    """
)
st.image(
    "./assets/flow_02.jpg",
    caption = "Answers user queries based on pre-loaded set of 3 PDF documents. Pre-retrieval is improved through semantic chunking. Post-retrieval process is improved through filtering by score threshold. Query is also checked for relevance to the pre-loaded subject matter loaded."
)
st.markdown(
    """
    1. It loads 3 PDF files downloaded from the GeBiz website: (i) a comprehensive guide on government procurement; (ii) a specific list of debarment or disqualification grounds; as well as (iii) registration lines.  
    2. The PDF files are stored in ./data folder, referenced through a list, and loaded using PyPDFLoader. 
    3. The PDF files are then split, chunked and stored in a vector database (Chroma). The pre-retrieval process is augmented by Semantic Chunking.  
    4. Sample queries are provided to guide the user on the type of query to input.
    5. When processing the user query, the system is given a template to answer succinctly, and only from the database.
    6. When processing the user query, the post-retrieval process is improved through filtering by score threshold. The score threshold is set at 0.5 to only retrieve documents above that threshold.  
    7. Retrieval-Augmented Generation is applied to the user query with the help of LangChain.  
    8. When returning the answer, if "context" does not exist, it would imply that the LLM is unable to find or match the query to the semantic chunks. A standard reply is given to request the user re-phrase the query.  
    9. The best-matched retrieved output is then printed below the query box.
    """
)
st.subheader(" ")

st.subheader("II. Exploring Procurement Data")
st.markdown(
    """
    This app assists the user in their queries on historical procurement data.
    """
)
st.image(
    "./assets/flow_01.jpg",
    caption = "Answers user queries based on their preferred set of filtered information. Transforms user query to improve clarity. Use of pandas DataFrame agent to analyse data and answer query."
)
st.markdown(
    """
    1. It loads a CSV file downloaded from the data.gov.sg relating to historical procurement data from GeBiz, for the period of FY2019 to FY2023.  
    2. Users are able to filter the information by selecting one or more agencies, as well as status of the tenders. 
    3. Depending on selections made, an empty set may exist. Users will be prompted to select at least one agency AND one status in order to ensure there is a valid set of data to display.  
    4. Users are able to apply queries on the filtered set of data.  
    5. The query is transformed by parsing it through an LLM query to improve its clarity.  
    6. A pandas DataFrame agent will analyse the filtered data, the clarified user query, and print the output.  
    """
)
