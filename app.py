import pandas as pd
import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine species prediction")
st.info("This is end-to-end Machine Learning app")

with st.expander("Data"):
    pass

with st.expander("Data Visualization"):
    pass

with st.expander("Input Data"):
    pass

with st.expander("Data preparation"):
    pass

with st.sidebar:
    st.header("Input Variables")
    island = st.selectbox("Island", ("Biscoe","Dream", "Torgersen"))
    bill_length_mm = st.slider("Bill length (mm)", 32.1, 59.6, 43.9)