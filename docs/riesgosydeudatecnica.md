# Riesgos y Deuda Técnica - CHATBOTRENTAVEHICULOS

## 1. Introducción

Durante el desarrollo de CHATBOTRENTAVEHICULOS se identificaron diferentes riesgos técnicos y elementos de deuda técnica que pueden afectar la evolución del sistema.

La identificación temprana de estos elementos permite establecer acciones de mitigación.

---

## 2. Riesgos Técnicos

| Riesgo | Categoría | Probabilidad | Impacto | Nivel |
|---|---|---|---|---|
| Pérdida de datos al reiniciar | Datos | Alta | Alto | Crítico |
| Falta de autenticación | Seguridad | Alta | Alto | Crítico |
| Asistente limitado | IA | Media | Medio | Medio |
| Falta de pruebas automatizadas | Calidad | Media | Medio | Medio |
| Errores de conexión API | Integración | Media | Medio | Medio |
| Falta de despliegue | Infraestructura | Media | Medio | Medio |

---

## 3. Descripción de los Riesgos

### 3.1 Pérdida de Datos

Actualmente los datos se almacenan en memoria.

Si la aplicación se reinicia, la información puede perderse.

#### Mitigación

Integrar una base de datos persistente.

---

### 3.2 Falta de Autenticación

Actualmente no existe un sistema de usuarios y contraseñas.

Esto representa un riesgo de seguridad.

#### Mitigación

Implementar:

- Registro de usuarios.
- Inicio de sesión.
- Roles.
- Control de permisos.

---

### 3.3 Asistente Limitado

El asistente actualmente responde principalmente a preguntas contempladas mediante palabras clave.

#### Mitigación

Implementar técnicas más avanzadas de procesamiento de lenguaje natural.

---

### 3.4 Falta de Pruebas Automatizadas

Actualmente se realizan principalmente pruebas manuales.

#### Mitigación

Crear:

- Pruebas unitarias.
- Pruebas de integración.
- Pruebas de endpoints.

---

## 4. Deuda Técnica

### 4.1 Datos en Memoria

La aplicación utiliza listas de Python en lugar de una base de datos.

Esto facilita el desarrollo inicial, pero limita la persistencia.

---

### 4.2 Lógica de Negocio Simplificada

Parte de la lógica se encuentra directamente relacionada con las consultas.

Se requiere una mejor separación de responsabilidades.

---

### 4.3 Ausencia de Configuración Externa

La configuración todavía se encuentra principalmente dentro del código.

Se recomienda utilizar variables de entorno.

---

### 4.4 Ausencia de Registro de Eventos

El sistema no cuenta con un sistema completo de logs.

Esto dificulta el diagnóstico de errores.

---

## 5. Plan de Reducción de Deuda Técnica

| Deuda | Acción |
|---|---|
| Datos en memoria | Integrar base de datos |
| Lógica mezclada | Separar servicios |
| Sin autenticación | Implementar sistema de usuarios |
| Sin pruebas | Crear pruebas automatizadas |
| Sin logs | Implementar logging |
| Sin despliegue | Utilizar Docker |

---

## 6. Priorización

### Alta Prioridad

- Base de datos.
- Autenticación.
- Pruebas.

### Prioridad Media

- Mejorar IA.
- Implementar logs.
- Separar lógica.

### Prioridad Baja

- Mejoras visuales.
- Funciones adicionales.

---

## 7. Conclusión

La deuda técnica identificada es esperada en una etapa de prototipo.

El objetivo del proyecto es reducir progresivamente estos elementos mediante la implementación de una arquitectura más estructurada.