import streamlit as st

st.title("ONA CH CDMX dev")
st.write(
    "Pagina web dedicada al ONA (fase de desarrollo)[docs.streamlit.io](https://docs.streamlit.io/)."
)


# Título de la aplicación
st.title('Formulario con ComboBox')

# ComboBox
opciones = ['','JAIME RAMIREZ PEREZ', 'PEDRO MAURICIO JAVIER PEREZ', 'ALMIDON PORFIRIO DIAZ ENLACE']
seleccion = st.selectbox('Selecciona una opción', opciones)

# Mostrar la opción seleccionada
st.write(f'Has seleccionado: {seleccion}')




