import streamlit as st
import pandas as pd
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="Sistema Inteligente de Renta de Vehículos",
    page_icon="🚗",
    layout="wide"
)


# =====================================
# ESTILOS PERSONALIZADOS
# =====================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f5f5;
}

/* Títulos */

h1 {
    color: #B71C1C !important;
    text-align: center;
}

h2, h3 {
    color: #B71C1C !important;
}

/* Texto normal */

p, label, div {
    color: #222222;
}

/* Métricas */

[data-testid="stMetric"] {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.15);
}

/* Inputs */

.stTextInput input,
.stTextArea textarea {
    background-color: white;
    color: black;
    border-radius: 10px;
    border: 2px solid #B71C1C;
}

/* Selectbox */

.stSelectbox div {
    color: black;
}

/* Botones */

.stButton button {
    background-color: #C62828;
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    height: 45px;
}

.stButton button:hover {
    background-color: #8E0000;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background-color: #B71C1C;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# DATOS SIMULADOS
# =====================================

if "clientes" not in st.session_state:

    st.session_state.clientes = [
        {
            "nombre": "Carlos Martinez",
            "vehiculo": "Toyota Hilux",
            "precio": 65,
            "estado": "Pendiente"
        },
        {
            "nombre": "Ana Gomez",
            "vehiculo": "Hyundai Tucson",
            "precio": 50,
            "estado": "Pendiente"
        },
        {
            "nombre": "Luis Perez",
            "vehiculo": "Toyota Prado",
            "precio": 90,
            "estado": "Pagado"
        },
        {
            "nombre": "Maria Hernandez",
            "vehiculo": "Ford Ranger",
            "precio": 70,
            "estado": "Pagado"
        },
        {
            "nombre": "Jose Ramirez",
            "vehiculo": "Volkswagen Jetta",
            "precio": 45,
            "estado": "Pendiente"
        }
    ]


if "vehiculos" not in st.session_state:

    st.session_state.vehiculos = [

        {
            "modelo": "Toyota Corolla",
            "estado": "Disponible",
            "precio": 35
        },

        {
            "modelo": "Nissan Versa",
            "estado": "Disponible",
            "precio": 30
        },

        {
            "modelo": "Kia Rio",
            "estado": "Disponible",
            "precio": 28
        },

        {
            "modelo": "Hyundai Tucson",
            "estado": "Alquilado",
            "precio": 50
        },

        {
            "modelo": "Toyota Hilux",
            "estado": "Alquilado",
            "precio": 65
        },

        {
            "modelo": "Chevrolet Spark",
            "estado": "Disponible",
            "precio": 25
        },

        {
            "modelo": "Mazda CX-5",
            "estado": "Disponible",
            "precio": 55
        },

        {
            "modelo": "Ford Ranger",
            "estado": "Alquilado",
            "precio": 70
        },

        {
            "modelo": "Honda Civic",
            "estado": "Disponible",
            "precio": 40
        },

        {
            "modelo": "Mitsubishi L200",
            "estado": "Disponible",
            "precio": 68
        },

        {
            "modelo": "Suzuki Swift",
            "estado": "Disponible",
            "precio": 27
        },

        {
            "modelo": "Volkswagen Jetta",
            "estado": "Alquilado",
            "precio": 45
        },

        {
            "modelo": "Kia Sportage",
            "estado": "Disponible",
            "precio": 58
        },

        {
            "modelo": "Hyundai Accent",
            "estado": "Disponible",
            "precio": 32
        },

        {
            "modelo": "Toyota Prado",
            "estado": "Alquilado",
            "precio": 90
        }

    ]


# =====================================
# VARIABLES
# =====================================

vehiculos = st.session_state.vehiculos

clientes = st.session_state.clientes


total_vehiculos = len(vehiculos)

disponibles = len(
    [
        v for v in vehiculos
        if v["estado"] == "Disponible"
    ]
)

alquilados = len(
    [
        v for v in vehiculos
        if v["estado"] == "Alquilado"
    ]
)


# =====================================
# TÍTULO
# =====================================

st.title(
    "🚗 Sistema Inteligente de Renta de Vehículos"
)

st.markdown(
    """
    <center>
    <p>
    Panel administrativo con asistente virtual inteligente
    </p>
    </center>
    """,
    unsafe_allow_html=True
)


# =====================================
# ESTADÍSTICAS
# =====================================

st.markdown("## 📊 Estadísticas del Sistema")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🚗 Total Vehículos",
        total_vehiculos
    )


with col2:

    st.metric(
        "✅ Disponibles",
        disponibles
    )


with col3:

    st.metric(
        "🔴 Alquilados",
        alquilados
    )


with col4:

    st.metric(
        "👥 Clientes",
        len(clientes)
    )


# =====================================
# TABLA DE VEHÍCULOS
# =====================================

st.markdown("---")

st.markdown(
    "## 🚘 Inventario de Vehículos"
)


df_vehiculos = pd.DataFrame(
    vehiculos
)


df_vehiculos.columns = [
    "Modelo",
    "Estado",
    "Precio por Día"
]


st.dataframe(
    df_vehiculos,
    use_container_width=True,
    hide_index=True
)


# =====================================
# PANEL LATERAL
# =====================================

with st.sidebar:

    st.title(
        "🚗 Menú"
    )

    st.markdown("---")

    opcion = st.radio(
        "Seleccione una opción:",
        [
            "🤖 Asistente Virtual",
            "🚘 Vehículos",
            "👥 Clientes",
            "📅 Reservas"
        ]
    )


# =====================================
# ASISTENTE VIRTUAL
# =====================================

if opcion == "🤖 Asistente Virtual":

    st.markdown("---")

    st.header(
        "🤖 Asistente Virtual"
    )

    st.info(
        "Realiza consultas sobre vehículos, clientes y reservas."
    )

    pregunta = st.text_area(
        "Escribe tu consulta:",
        placeholder=(
            "Ejemplo: ¿Qué vehículos están disponibles?"
        ),
        height=100
    )


    if st.button(
        "🔍 Consultar Asistente"
    ):

        if pregunta.strip() == "":

            st.warning(
                "Por favor, escribe una pregunta."
            )

        else:

            try: 
                #conexion con api

                respuesta = requests.post(

                    f"{API_URL}/ask",

                    json={
                        "pregunta": pregunta
                    },

                    timeout=10

                )


                if respuesta.status_code == 200:

                    datos = respuesta.json()


                    st.success(
                        "Respuesta del asistente"
                    )


                    st.write(
                        datos["respuesta"]
                    )


                else:

                    st.error(
                        f"Error de la API: "
                        f"{respuesta.status_code}"
                    )


            except Exception as e:

                st.error(
                    f"No se pudo conectar con la API: {e}"
                )


# =====================================
# VEHÍCULOS
# =====================================

elif opcion == "🚘 Vehículos":

    st.header(
        "🚘 Gestión de Vehículos"
    )

    st.dataframe(
        df_vehiculos,
        use_container_width=True,
        hide_index=True
    )


# =====================================
# CLIENTES
# =====================================

elif opcion == "👥 Clientes":

    st.header(
        "👥 Clientes Registrados"
    )


    df_clientes = pd.DataFrame(
        clientes
    )


    st.dataframe(
        df_clientes,
        use_container_width=True,
        hide_index=True
    )


# =====================================
# RESERVAS
# =====================================

elif opcion == "📅 Reservas":

    st.header(
        "📅 Reservas del Sistema"
    )


    st.info(
        "Actualmente existen 5 reservas registradas."
    )


# =====================================
# PIE DE PÁGINA
# =====================================

st.markdown("---")

st.caption(
    "Sistema Inteligente de Renta de Vehículos | "
    "Asistente Virtual conectado mediante API FastAPI"
)