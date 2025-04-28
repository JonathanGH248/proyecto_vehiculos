import pandas as pd
import plotly.express as px
import streamlit as st

# Encabezado de la app
st.header('Análisis de Datos de Vehículos')

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para mostrar histograma
build_histogram = st.checkbox('Mostrar histograma de precios')

# Casilla de verificación para mostrar gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión Precio vs Año')

# Si se selecciona la casilla del histograma
if build_histogram:
    st.write('Creación del histograma de precios de los vehículos')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

# Si se selecciona la casilla del gráfico de dispersión
if build_scatter:
    st.write('Creación del gráfico de dispersión Precio vs Año')
    fig2 = px.scatter(car_data, x="model_year", y="price")
    st.plotly_chart(fig2, use_container_width=True)