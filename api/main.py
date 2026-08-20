from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from api.schemas import PreguntaRequest

import os
import requests
import logging
import time
import uuid
from dotenv import load_dotenv

load_dotenv()

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

AI_VERSION = "ollama-llama3.2"

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
        "modelo": "Nissan Versa",
        "estado": "Disponible"
    },
    {
        "modelo": "Kia Rio",
        "estado": "Disponible"
    },
    {
        "modelo": "Hyundai Tucson",
        "estado": "Alquilado"
    },
    {
        "modelo": "Toyota Hilux",
        "estado": "Alquilado"
    },
    {
        "modelo": "Chevrolet Spark",
        "estado": "Disponible"
    },
    {
        "modelo": "Mazda CX-5",
        "estado": "Disponible"
    },
    {
        "modelo": "Ford Ranger",
        "estado": "Alquilado"
    },
    {
        "modelo": "Honda Civic",
        "estado": "Disponible"
    },
    {
        "modelo": "Mitsubishi L200",
        "estado": "Disponible"
    },
    {
        "modelo": "Suzuki Swift",
        "estado": "Disponible"
    },
    {
        "modelo": "Volkswagen Jetta",
        "estado": "Alquilado"
    },
    {
        "modelo": "Kia Sportage",
        "estado": "Disponible"
    },
    {
        "modelo": "Hyundai Accent",
        "estado": "Disponible"
    },
    {
        "modelo": "Toyota Prado",
        "estado": "Alquilado"
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
# CONEXIÓN CON OLLAMA
# ==========================

OLLAMA_URL = os.getenv(
    "OLLAMA_URL",
    "http://localhost:11434/api/generate"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:latest"
)


def consultar_ollama(pregunta, contexto):
    prompt = f"""
Eres un asistente virtual para una empresa de renta de vehículos.

Tu función es ayudar a los administradores con información sobre
vehículos, clientes y reservas.

Utiliza únicamente la información proporcionada en el contexto.

Si la información necesaria no aparece en el contexto, indica que
no tienes esa información disponible.

Contexto del sistema:
{contexto}

Pregunta del usuario:
{pregunta}

Responde de manera clara, natural y breve en español.
"""

    respuesta = requests.post(
        OLLAMA_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    respuesta.raise_for_status()

    datos = respuesta.json()

    return datos["response"].strip()
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

    pregunta = request.pregunta

    vehiculos_disponibles = [
        v["modelo"]
        for v in vehiculos
        if v["estado"] == "Disponible"
    ]

    vehiculos_alquilados = [
        v["modelo"]
        for v in vehiculos
        if v["estado"] == "Alquilado"
    ]

    contexto = f"""
INFORMACIÓN OFICIAL DEL SISTEMA DE RENTA DE VEHÍCULOS

VEHÍCULOS DISPONIBLES:
{chr(10).join("- " + v for v in vehiculos_disponibles)}

VEHÍCULOS ALQUILADOS:
{chr(10).join("- " + v for v in vehiculos_alquilados)}

CLIENTES REGISTRADOS:
{clientes}

RESERVAS REGISTRADAS:
{reservas}
"""

    try:

        respuesta_ia = consultar_ollama(
            pregunta,
            contexto
        )

        return {
            "pregunta": pregunta,
            "tipo_consulta": "ia_ollama",
            "respuesta": respuesta_ia
        }

    except Exception as error:

        logger.error(
            "Error al consultar Ollama: %s",
            error
        )

        # Si Ollama falla, mantenemos el chatbot anterior
        resultado = chatbot(pregunta)

        return {
            "pregunta": pregunta,
            "tipo_consulta": resultado["tipo_consulta"],
            "respuesta": resultado["respuesta"]
        }