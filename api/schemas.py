from pydantic import BaseModel, Field


class PreguntaRequest(BaseModel):
    pregunta: str = Field(
        ...,
        min_length=1,
        description="Pregunta del usuario sobre la renta de vehículos"
    )