import streamlit as st
import numpy as np
from joblib import load
model = load('model_opossum.joblib')
# ---------------------------------------------------------------------
# Config streamlit
#-----------------------------------------------------------------------------------
st.set_page_config(page_title="Opossum Predict", page_icon=":dart:", layout="wide")

st.title("Estimateur d'age d'un opossum")

col1, col2, col3 = st.columns(3)
with col1:
    a = st.slider('Longueur de tête',82.0,104.0,step=0.1)
with col2:
    b = st.slider('Largeur du crâne',50.0,70.0,step=0.1)
with col3:
    c = st.slider('Longueur totale',75.0,97.0,step=0.1)

col1, col2, col3 = st.columns(3)
with col1:
    d = st.slider('Longueur du pied',60.0,80.0,step=0.1)
with col2:
    e = st.slider('Longueur de la conque auriculaire',40.0,57.0,step=0.1)
with col3:
    f = st.slider('Tour de ventre',25.0,40.0,step=0.1)


if st.button("Estimer l'age"):
    result = model.predict(np.array([a,b,c,d,e,f]).reshape(1,6))[0]
    annee = int(result)
    mois = int(result%1*12)
    st.subheader(f"L'age de l'opossum est d'environ {annee} ans et {mois} mois.")