import pandas as pd
import streamlit as st
import numpy as np
import io
from sklearn.ensemble import RandomForestClassifier

st.title("Penguine species prediction")
st.info("This is end-to-end Machine Learning app")

with st.expander("Data"):
    st.write("**Raw data**")
    df = pd.read_csv("data/penguins_cleaned.csv")
    df

    st.write("Input variables")
    X_raw = df.drop("species", axis=1)
    X_raw

    st.write("Target variable")
    y_raw = df.species
    y_raw
    
    st.write("Descriptive Statistics")
    desc = df.describe()
    desc

    st.write("More information about Data")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_string = buffer.getvalue()
    st.markdown(info_string)

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
    bill_depth_mm = st.slider("Bill depth (mm)", 13.1, 21.5, 17.2)
    flipper_depth_mm = st.slider("Flipper depth (mm)", 172.0, 231.0, 201.0)
    body_mass_g = st.slider("Body mass (g)", 2700.0, 6300.0, 4207.0)
    gender = st.selectbox("Gender", ("male", "female"))