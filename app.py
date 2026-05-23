import streamlit as st

st.title("Mi primera aplicación en Python")

st.sidebar.title("Parámetros")

st.write("Elaborado por : Jorge Huaman")

st.sidebar.image("dmclogo.png")

sesion = st.sidebar.selectbox("Seleccione una sesion", ["Sesion 1","Sesion 2","Sesion 3","Sesion 4"])

if sesion == "Sesion 1":
  st.write("Bienvenido a la sesion 1")
  st.image("pythonlogo.png")
  
elif sesion == "Sesion 2":
  st.write("Bienvenido a la sesion 2")  
elif sesion == "Sesion 3":
  st.write("Bienvenido a la sesion 3")
elif sesion == "Sesion 4":
  st.write("Bienvenido a la sesion 4")
