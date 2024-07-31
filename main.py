# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:32:44 2024

@author: asus
"""

# main.py

import subprocess
import streamlit as st

# Run FastAPI app
subprocess.Popen(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])

# Streamlit UI
st.title("Diabetes Prediction API")

st.write("This app serves the Diabetes Prediction API using FastAPI.")
st.write("Use the `/docs` endpoint to interact with the API documentation.")
