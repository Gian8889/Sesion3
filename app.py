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

  precio = st.number_input("Ingrese el precio del producto", min_value = 0, max_value = 5000, value = 1200)
  descuento = st.number_input("Ingrese el descuento del producto del 0 al 100%", min_value=0, max_value=100)

  precio_final_producto = precio - (precio*descuento/100)

  st.write("El producto final del producto es: ", precio_final_producto)
elif sesion == "Sesion 3":
  st.write("Bienvenido a la sesion 3")
elif sesion == "Sesion 4":
  st.write("Bienvenido a la sesion 4")
