import streamlit as st
import pandas as pd
import numpy as np

# Project page title
st.set_page_config(
    page_title="CPF Policies Guide",
    page_icon=":material/group:",
)

# Mandatory disclaimer for project
EXPANDER_NOTICE = """
**IMPORTANT NOTICE**: This web application is a prototype developed for **educational purposes** only.
The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

**Furthermore, please be aware that the LLM may generate inaccurate or incorrect information.
You assume full responsibility for how you use any generated output.**

Always consult with qualified professionals for accurate and personalised advice.
"""

expander = st.expander(":red[Disclaimer]", True)
expander.write(EXPANDER_NOTICE)

# Give the main page a header
st.write("# Welcome to your friendly guide on understanding CPF policies")

# Manifest sidebar
st.sidebar.success("Select a demo above.")

