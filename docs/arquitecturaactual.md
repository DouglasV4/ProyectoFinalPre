# 2. Arquitectura actual.md

markdown
# Arquitectura Actual - CHATBOTRENTAVEHICULOS

## 1. Introducción

RentCar AI es un prototipo de sistema inteligente para la administración de una empresa de renta de vehículos.

Actualmente, la aplicación permite consultar información relacionada con vehículos, clientes y reservas mediante una interfaz web y un asistente virtual.

---

## 2. Arquitectura Actual

La arquitectura actual está compuesta por:

- Interfaz web desarrollada con Streamlit.
- API REST desarrollada con FastAPI.
- Asistente virtual.
- Datos simulados almacenados en memoria.
- Comunicación mediante solicitudes HTTP.

---

## 3. Diagrama de Arquitectura Actual

text
+----------------------+
|       USUARIO        |
+----------+-----------+
           |
           v
+----------------------+
|     STREAMLIT        |
|    Interfaz Web      |
+----------+-----------+
           |
           | HTTP Request
           v
+----------------------+
|       FASTAPI        |
|       API REST       |
+----------+-----------+
           |
           v
+----------------------+
|   PROCESAMIENTO DE   |
|      CONSULTAS       |
+----------+-----------+
           |
           v
+----------------------+
|    DATOS SIMULADOS   |
+----------------------+
| Vehículos            |
| Clientes             |
| Reservas             |
+----------------------+