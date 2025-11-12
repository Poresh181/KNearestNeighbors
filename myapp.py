import streamlit as st
import numpy as np
import pandas as pd

st.title("K-Nearest Neighbors-Build & Deploy(Streamlit)")
st.sidebar.header("Dataset & Preprocessing")

from sklearn.datasets import load_iris, load_wine, load_breast_cancer
def load_sample(name):
  if name == "Iris":
    df = load_iris(as_frame=True)
  elif name == "Wine":
    df = load_wine(as_frame=True)
  elif name == "Breast Cancer":
    df = load_breast_cancer(as_frame=True)
  else:
    return None

  df = pd.concat([df.frame.reset_index(drop=True)], axis=1)
  return df

  data_source = st.sidebar.selectbox("Data Source", ["Upload CSV","Sample dataset(Iris)", "Sample dataset(Wine)", "Sample dataset(Breast Cancer)"])
    

