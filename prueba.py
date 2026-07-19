import gradio as gr

def chatbot(pregunta):

    pregunta = pregunta.lower()

    if "disponible" in pregunta:
        return """
 Vehículos disponibles:

- Toyota Corolla
- Hyundai Tucson
- Nissan Versa
- Kia Rio
"""

    elif "reserva" in pregunta:
        return " Actualmente existen 5 reservas registradas."

    elif "cliente" in pregunta:
        return " Actualmente existen 18 clientes registrados."

    elif "precio" in pregunta:
        return " El precio de alquiler depende del vehículo seleccionado."

    else:
        return " Lo siento, aún estoy en desarrollo y no puedo responder esa consulta."

demo = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Escribe tu consulta..."
    ),
    outputs="text",
    title="Asistente Inteligente para Renta de Vehículos",
    description="Chatbot de apoyo para dueños y secretaria."
)

demo.launch()