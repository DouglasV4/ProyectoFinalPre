# Arquitectura Objetivo - CHATBOTRENTADEVEHICULOS

## 1. Introducción

La arquitectura objetivo de RentCar AI representa la evolución esperada del prototipo actual hacia una aplicación más estructurada, escalable, segura y mantenible.

El objetivo es separar claramente la interfaz de usuario, la lógica de negocio, la inteligencia artificial, la persistencia de datos y los servicios de infraestructura.

---

## 2. Objetivo de la Arquitectura

La arquitectura objetivo busca:

- Separar la interfaz del backend.
- Centralizar la lógica de negocio mediante una API.
- Incorporar una base de datos persistente.
- Mejorar el asistente virtual.
- Implementar autenticación y autorización.
- Incorporar pruebas automatizadas.
- Facilitar el despliegue de la aplicación.
- Incorporar monitoreo y registro de eventos.

---

## 3. Diagrama de Arquitectura Objetivo

```text
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
           | HTTP / REST
           v
+----------------------+
|       FASTAPI        |
|       API REST       |
+----------+-----------+
           |
     +-----+------+
     |            |
     v            v
+----------+  +----------------+
| LÓGICA   |  | SERVICIO DE IA |
| NEGOCIO  |  | NLP / CHATBOT  |
+----+-----+  +--------+-------+
     |                 |
     +--------+--------+
              |
              v
     +------------------+
     |    BASE DE DATOS |
     +------------------+
     |                  |
     v                  v
+------------+    +------------+
| Vehículos  |    | Clientes   |
+------------+    +------------+
     |
     v
+------------+
| Reservas   |
+------------+

              |
              v

     +------------------+
     | MONITOREO Y LOGS |
     +------------------+