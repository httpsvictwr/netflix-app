import streamlit as st
import pandas as pd

st.title("Netflix app")

@st.cache_data
def cargar_datos():
    return pd.read_csv("movies.csv", encoding="latin-1")

data = cargar_datos()
st.text("Creado por: Victor, Rosiely, Diego")

# ---------- SIDEBAR ----------
mostrar_todos = st.sidebar.checkbox("Mostrar todos las peliculas")

titulo = st.sidebar.text_input("Título de la pelicula :")
btn_buscar = st.sidebar.button("Buscar peliculas")

directores = sorted(data["director"].dropna().unique())
director = st.sidebar.selectbox("Seleccionar Director", directores)
btn_director = st.sidebar.button("Filtrar director")

# ---------- FUNCIONES ----------
def buscar_por_titulo(df, texto):
    return df[df["name"].str.contains(texto, case=False, na=False)]

def filtrar_por_director(df, nombre):
    return df[df["director"] == nombre]

# ---------- CONTENIDO PRINCIPAL ----------
if mostrar_todos:
    st.subheader("Todas las peliculas")
    st.dataframe(data)

elif btn_buscar:
    resultado = buscar_por_titulo(data, titulo)
    st.write(f"Total de peliculas mostradas : {len(resultado)}")
    st.dataframe(resultado)

elif btn_director:
    resultado = filtrar_por_director(data, director)
    st.write(f"Total peliculas : {len(resultado)}")
    st.dataframe(resultado)