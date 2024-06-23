
from pydantic import BaseModel

class TranscriptionResponse(BaseModel):
    transcription: str
    summary: str
    timestamps: dict
