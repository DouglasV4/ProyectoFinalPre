from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from api.schemas import PreguntaRequest

import logging
import time
import uuid

# ==========================
# APLICACIÓN
# ==========================

app = FastAPI(
    title="API Sistema Inteligente para Renta de Vehículos",
    description="API para consultar información sobre vehículos, clientes y reservas",
    version="1.0.0"
)

# ==========================
# OBSERVABILIDAD
# ==========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("rentcar_api")

AI_VERSION = "rules-v1"

@app.middleware("http")
async def observability_middleware(request, call_next):

    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    try:

        response = await call_next(request)

        duration_ms = (
            time.perf_counter() - start_time
        ) * 1000

        error_type = (
      "validation_error"
            if response.status_code == 422
            else None
        )
        logger.info(
            "request_id=%s | endpoint=%s | method=%s | "
            "status=%s | duration_ms=%.2f | "
            "ai_version=%s | error_type=%s",
            request_id,
            request.url.path,
            request.method,
            response.status_code,
            duration_ms,
            AI_VERSION,
            error_type
        )

        response.headers["X-Request-ID"] = request_id

        return response

    except Exception as error:

        duration_ms = (
            time.perf_counter() - start_time
        ) * 1000

        logger.error(
            "request_id=%s | endpoint=%s | method=%s | "
            "status=500 | duration_ms=%.2f | "
            "ai_version=%s | error_type=%s",
            request_id,
            request.url.path,
            request.method,
            duration_ms,
            AI_VERSION,
            type(error).__name__
        )

        raise

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