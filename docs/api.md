# API - Sistema Inteligente de Renta de Vehículos

## Descripción

La API permite conectar la interfaz visual desarrollada con Streamlit con la lógica del sistema de renta de vehículos.

Su función principal es recibir preguntas del usuario, procesarlas y devolver información relacionada con:

- Vehículos disponibles.
- Vehículos alquilados.
- Clientes registrados.
- Reservas realizadas.

La API fue desarrollada utilizando *FastAPI*.

---

## Arquitectura

La comunicación del sistema funciona de la siguiente manera:

Usuario
↓
Streamlit (app.py)
↓
Petición HTTP POST
↓
FastAPI (api/main.py)
↓
Procesamiento de la consulta
↓
Respuesta JSON
↓
Streamlit muestra la respuesta

---

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Pydantic
- Requests
- Streamlit

---

## Estructura de la API

```text
api/
│
├── main.py
│
└── schemas.py