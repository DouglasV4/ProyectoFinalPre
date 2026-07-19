# RentCar AI - Sistema Inteligente para la Administración de Renta de Vehículos

## 1. Información General

**Módulo:** Módulo 4 - Desarrollo de Aplicaciones con IA\
**Semana:** Semana 1 - Diagnóstico y arquitectura inicial\
**Nombre del equipo:** RentaCar

**Integrantes:** - Douglas Jose Velasquez Vasquez 
                 - carlos Antonio 
                 - Jose Elias Escobar Ortiz 


------------------------------------------------------------------------

## 2. Descripción del Problema

Muchas empresas de renta de vehículos administran clientes, vehículos y
pagos de forma manual, lo que provoca pérdida de tiempo y errores. El
proyecto propone un sistema inteligente que centraliza la información y
permite consultar datos mediante un asistente virtual administrativo.

------------------------------------------------------------------------

## 3. Usuarios o Beneficiarios

  Usuario      Necesidad               Cómo ayuda
  ------------ ----------------------- -------------------------------------
  Dueño        Supervisar el negocio   Consulta reportes y disponibilidad.
  Secretaria   Registrar alquileres    Automatiza registros y pagos.
  Cliente      Atención rápida         Reduce tiempos de gestión.

------------------------------------------------------------------------

## 4. Descripción de la Solución

Aplicación web desarrollada con Python y Streamlit para administrar
vehículos, clientes, alquileres y pagos. Incluye un asistente virtual
que responde preguntas como: - ¿Cuántos vehículos están alquilados? -
¿Qué clientes tienen pagos pendientes? - ¿Qué vehículos están
disponibles?

Entradas: datos de clientes, vehículos, pagos y consultas del usuario.

Salidas: reportes, estado de vehículos y respuestas del asistente.

------------------------------------------------------------------------

## 5. Componente de IA

  Elemento       Descripción
  -------------- ------------------------------------------------------
  Tipo de IA     Procesamiento de Lenguaje Natural (NLP)
  Técnica        Asistente virtual basado en interpretación de texto
  Entrada        Consultas del usuario
  Salida         Respuestas administrativas automáticas
  Evaluación     Validación de respuestas según los datos registrados
  Limitaciones   Responde consultas contempladas por el sistema

La IA permite consultar información administrativa utilizando lenguaje
natural.

------------------------------------------------------------------------

## 6. Estado Actual del Proyecto

### Funcionalidades implementadas

-   Registro de clientes y alquileres.
-   Gestión de vehículos.
-   Asistente virtual administrativo.

### Pendientes

-   Base de datos.
-   Autenticación.
-   IA más avanzada.

### Evidencias

-   Capturas del sistema.
-   Ejecución en Streamlit.

------------------------------------------------------------------------

## 7. Arquitectura Actual

  Componente           Descripción         Estado
  -------------------- ------------------- -----------------
  Interfaz             Streamlit           Implementado
  Backend              Python              Implementado
  IA                   Asistente virtual   Implementado
  Datos                Listas simuladas    Implementado
  Servicios externos   Ninguno             No implementado
  Configuración        requirements.txt    Implementado

Diagrama:

Usuario → Streamlit → Backend Python → Asistente → Datos → Respuesta

------------------------------------------------------------------------

## 8. Arquitectura Objetivo

Objetivo:

Usuario → Streamlit → API → Motor IA → Base de Datos → Respuesta

Se espera integrar API, base de datos, pruebas, despliegue y monitoreo.

------------------------------------------------------------------------

## 9. Estructura del Repositorio

``` text
 CHATBOTRENTAVEHICULOS/
│ app.py
│ README.md
│ requirements.txt
├── docs/
    -api.md
    -arquitectura objetivo
├── data/
├── images/
└── tests/
```

------------------------------------------------------------------------

## 10. Instalación y Ejecución

### Requisitos

-   Python 3.11
-   pip

### Instalación

``` bash
pip install -r requirements.txt
```

### Ejecución

``` bash
streamlit run app.py
```

Variables de entorno: No aplica.

------------------------------------------------------------------------

## 11. Datos Utilizados

  -----------------------------------------------------------------------
  Fuente            Tipo              Uso               Observaciones
  ----------------- ----------------- ----------------- -----------------
  Datos simulados   Clientes y        Pruebas           No contienen
                    vehículos                           datos sensibles

  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 12. Riesgos Técnicos

  Riesgo              Categoría   Probabilidad   Impacto   Mitigación
  ------------------- ----------- -------------- --------- -------------------
  Datos en memoria    Datos       Alta           Alto      Integrar BD
  IA limitada         Modelo      Media          Medio     Mejorar modelo
  Sin autenticación   Seguridad   Alta           Alto      Implementar login

------------------------------------------------------------------------

## 13. Plan de Mejora por semana

  Semana   Mejora                      Evidencia
  -------- --------------------------- --------------------
  2        API inteligente             Endpoint
  3        Pruebas                     Tests
  4        Despliegue                  Docker
  5        Monitoreo                   Logs
  6        Seguridad y documentación   Presentación final

------------------------------------------------------------------------

## 14. Limitaciones Actuales

-   Datos simulados.
-   Sin base de datos.
-   IA basada en reglas.

------------------------------------------------------------------------

## 15. Evidencias

  Evidencia   Ubicación   Descripción
  ----------- ----------- ----------------------
  Capturas    images/     Interfaz del sistema
  Código      app.py      Aplicación funcional

------------------------------------------------------------------------

## 16. Créditos y Referencias

-   Python
-   Streamlit
-   Pandas
-   Documentación oficial de Streamlit

------------------------------------------------------------------------

## 17. Checklist de revision

-   [x] Problema descrito.
-   [x] Usuarios identificados.
-   [x] IA documentada.
-   [x] Arquitectura incluida.
-   [x] Instalación explicada.
-   [x] Riesgos identificados.
-   [x] Plan de mejora definido.
