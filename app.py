import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por : Jorge Huaman")

sesion = st.sidebar.selectbox("Seleccione una sesion", ["Sesion 1","Sesion 2","Sesion 3","Sesion 4"])
