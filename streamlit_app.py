import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

st.title("Hello world!")

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")

st.header('This is a header with divider', divider='rainbow')

st.markdown("This is created using st.markdown")

st.subheader("st.columns")
col1, col2 = st.columns(2)

with col1:
    x = st.slider("Choose an x value",1,10)

with col2:
    st.write("The value of :red[***x***] is: ",x)

st.subheader("st.area_chart")
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
st.area_chart(df)
