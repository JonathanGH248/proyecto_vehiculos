import pandas as pd
import plotly.express as px
import streamlit as st

# Título principal
st.title('Análisis Interactivo de Vehículos Usados')

# Subtítulo
st.subheader('Explora los precios y años de los vehículos en venta')

# Divider visual
st.divider()

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear columnas para los dos gráficos
col1, col2 = st.columns(2)

# Primera columna: Histograma
with col1:
    st.subheader('Histograma de Precios')
    if st.checkbox('Mostrar Histograma'):
        fig = px.histogram(car_data, x="price", title="Distribución de precios")
        st.plotly_chart(fig, use_container_width=True)

# Segunda columna: Gráfico de Dispersión
with col2:
    st.subheader('Gráfico Precio vs Año')
    if st.checkbox('Mostrar Dispersión'):
        fig2 = px.scatter(car_data, x="model_year", y="price", title="Precio vs Año de Fabricación")
        st.plotly_chart(fig2, use_container_width=True)

# Divider final
st.divider()

# Footer
st.caption('Proyecto desarrollado como práctica de despliegue de apps con Streamlit.')