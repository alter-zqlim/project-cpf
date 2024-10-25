import streamlit as st

st.set_page_config(
    page_title = "Methodology", 
    page_icon = ":material/assistant_navigation:"
)

st.title("Methodology")

st.subheader("I. General Guide to Government Procurement")
st.markdown(
    """
    This app assists the user in their queries on government procurement in general.
    """
)
st.image(
    "./assets/street.jpg",
    caption = "Watercolour ink image of a flooded post-apocalyptic street lined with abandoned shophouses of varying heights and sizes. The sky is cloudy and rust red."
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
st.subheader("II. General Guide to Government Procurement")
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

st.subheader("A comprehensive explanation of the data flows and implementation details.")
st.subheader("A flowchart illustrating the process flow for each of the use cases in the application.")
st.subheader("For example, if the application has two main use cases: a) chat with information and b) intelligent search, each of these use cases should have its own flowchart.")

