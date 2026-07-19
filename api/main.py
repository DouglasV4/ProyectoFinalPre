from fastapi import FastAPI
from schemas import PreguntaRequest


# ==========================
# APLICACIÓN
# ==========================

app = FastAPI(
    title="API Sistema Inteligente para Renta de Vehículos",
    description="API para consultar información sobre vehículos, clientes y reservas",
    version="1.0.0"
)


# ==========================
# BASE DE DATOS SIMULADA
# ==========================

vehiculos = [
    {
        "modelo": "Toyota Corolla",
        "estado": "Disponible"
    },
    {
        "modelo": "Hyundai Tucson",
        "estado": "Alquilado"
    },
    {
        "modelo": "Nissan Versa",
        "estado": "Disponible"
    },
    {
        "modelo": "Kia Rio",
        "estado": "Disponible"
    }
]


clientes = 18

reservas = 5


# ==========================
# HEALTH CHECK
# ==========================

@app.get("/health")
def health():

    return {
        "status": "ok",
        "service": "API Sistema de Renta de Vehículos"
    }


# ==========================
# METADATA
# ==========================

@app.get("/metadata")
def metadata():

    return {
        "project": "Sistema Inteligente para Renta de Vehículos",
        "version": "1.0.0",
        "capacidad": "Chatbot de consulta sobre vehículos, clientes y reservas",
        "tipo_ia": "Asistente basado en reglas",
        "purpose": "Apoyar la consulta de información administrativa del sistema"
    }


# ==========================
# FUNCIÓN DEL CHATBOT
# ==========================

def chatbot(pregunta):

    pregunta = pregunta.lower()


    # ==========================
    # VEHÍCULOS DISPONIBLES
    # ==========================

    if "disponible" in pregunta:

        disponibles = []

        for v in vehiculos:

            if v["estado"] == "Disponible":

                disponibles.append(
                    v["modelo"]
                )

        return {
            "tipo_consulta": "vehiculos_disponibles",
            "respuesta": (
                "🚗 Vehículos disponibles:\n\n"
                + "\n".join(disponibles)
            )
        }


    # ==========================
    # VEHÍCULOS ALQUILADOS
    # ==========================

    elif "alquilado" in pregunta:

        alquilados = []

        for v in vehiculos:

            if v["estado"] == "Alquilado":

                alquilados.append(
                    v["modelo"]
                )

        return {
            "tipo_consulta": "vehiculos_alquilados",
            "respuesta": (
                "📋 Vehículos alquilados:\n\n"
                + "\n".join(alquilados)
            )
        }


    # ==========================
    # CLIENTES
    # ==========================

    elif "cliente" in pregunta:

        return {
            "tipo_consulta": "clientes",
            "respuesta": (
                f"👤 Actualmente existen "
                f"{clientes} clientes registrados."
            )
        }


    # ==========================
    # RESERVAS
    # ==========================

    elif "reserva" in pregunta:

        return {
            "tipo_consulta": "reservas",
            "respuesta": (
                f"📅 Actualmente existen "
                f"{reservas} reservas registradas."
            )
        }


    # ==========================
    # CONSULTA NO RECONOCIDA
    # ==========================

    else:

        return {
            "tipo_consulta": "ayuda",
            "respuesta": """
🤖 Consulta no encontrada.

Prueba preguntando:

- ¿Qué vehículos están disponibles?
- ¿Qué vehículos están alquilados?
- ¿Cuántos clientes hay?
- ¿Cuántas reservas hay?
"""
        }


# ==========================
# ENDPOINT PRINCIPAL
# ==========================

@app.post("/ask")
def ask(request: PreguntaRequest):

    resultado = chatbot(request.pregunta)

    return {
        "pregunta": request.pregunta,
        "tipo_consulta": resultado["tipo_consulta"],
        "respuesta": resultado["respuesta"]
    }