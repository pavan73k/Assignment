import os
import json
from whisper import load_model
from transformers import pipeline


whisper_model = load_model("large-v3")

summarization_pipeline = pipeline("summarization")

def transcribe_audio(file_path: str) -> str:
    try:
        result = whisper_model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        raise RuntimeError(f"Transcription failed: {str(e)}")

def summarize_text(text: str) -> str:
    try:
        summary = summarization_pipeline(text, max_length=150, min_length=30, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        raise RuntimeError(f"Summarization failed: {str(e)}")

def extract_timestamps(transcription: str) -> dict:
    
    timestamps = {"start": 0, "end": len(transcription)}
    return timestamps
