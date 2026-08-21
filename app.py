import streamlit as st
import pandas as pd
import requests
import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")


# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="RentCar AI",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================
# ESTILOS PROFESIONALES
# =====================================

st.markdown("""
<style>

    /* ================================
       CONFIGURACIÓN GENERAL
       ================================ */

    .stApp {
        background-color: #f4f6f8;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }


    /* ================================
       SIDEBAR
       ================================ */

    section[data-testid="stSidebar"] {
        background-color: #151922;
        border-right: 1px solid #252b36;
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] .stRadio label {
        padding: 10px 8px;
        border-radius: 8px;
    }


    /* ================================
       TITULOS
       ================================ */

    h1 {
        color: #151922 !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
    }

    h2, h3 {
        color: #202631 !important;
        font-weight: 700 !important;
    }

    p {
        color: #5f6875;
    }


    /* ================================
       ENCABEZADO
       ================================ */

    .brand-header {
        background: linear-gradient(
            135deg,
            #151922 0%,
            #242b38 100%
        );

        padding: 28px 32px;
        border-radius: 18px;
        margin-bottom: 25px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    }

    .brand-title {
        color: white;
        font-size: 32px;
        font-weight: 800;
        margin: 0;
    }

    .brand-subtitle {
        color: #c7cdd6;
        font-size: 15px;
        margin-top: 6px;
    }

    .system-status {
        background-color: #1f9d55;
        color: white;
        padding: 7px 13px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        display: inline-block;
        margin-top: 15px;
    }


    /* ================================
       TARJETAS DE ESTADÍSTICAS
       ================================ */

    [data-testid="stMetric"] {
        background-color: white;
        border: 1px solid #e4e7eb;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05);
    }

    [data-testid="stMetricLabel"] {
        color: #697382 !important;
        font-weight: 600;
    }

    [data-testid="stMetricValue"] {
        color: #151922 !important;
        font-weight: 800;
    }


    /* ================================
       CONTENEDORES
       ================================ */

    .dashboard-card {
        background-color: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e4e7eb;
        box-shadow: 0 5px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    .card-title {
        color: #202631;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 15px;
    }


    /* ================================
       BOTONES
       ================================ */

    .stButton > button {
        background-color: #c62828;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: 700;
        min-height: 42px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background-color: #a61f1f;
        color: white;
        transform: translateY(-1px);
    }


    /* ================================
       INPUTS
       ================================ */

    .stTextInput input,
    .stTextArea textarea {
        background-color: white;
        color: #202631;
        border: 1px solid #d9dee5;
        border-radius: 10px;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border-color: #c62828;
        box-shadow: 0 0 0 1px #c62828;
    }


    /* ================================
       TABLAS
       ================================ */

    [data-testid="stDataFrame"] {
        border-radius: 12px;
        overflow: hidden;
        border: 1px solid #e1e5ea;
    }


    /* ================================
       ESTADOS
       ================================ */

    .status-available {
        color: #18864b;
        font-weight: 700;
    }

    .status-rented {
        color: #c62828;
        font-weight: 700;
    }


    /* ================================
       DIVISORES
       ================================ */

    hr {
        border: none;
        border-top: 1px solid #e1e5ea;
        margin: 25px 0;
    }


    /* ================================
       PIE DE PÁGINA
       ================================ */

    .footer {
        text-align: center;
        color: #89919d;
        font-size: 13px;
        margin-top: 35px;
        padding-top: 20px;
        border-top: 1px solid #e1e5ea;
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

# =====================================
# ENCABEZADO PRINCIPAL
# =====================================

st.markdown("""
<div class="brand-header">
<div class="brand-title">🚗 RENTCAR AI</div>
<div class="brand-subtitle">Sistema inteligente de gestión de renta de vehículos</div>
<div class="system-status">● Sistema operativo · IA conectada</div>
</div>
""", unsafe_allow_html=True)


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