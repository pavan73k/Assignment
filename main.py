from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import shutil
import os

from .utils import transcribe_audio, summarize_text, extract_timestamps

app = FastAPI()

@app.post("/transcribe")
async def transcribe_audio_file(file: UploadFile):
    try:
       
        temp_dir = "temp"
        os.makedirs(temp_dir, exist_ok=True)
        file_path = os.path.join(temp_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
       
        transcription = transcribe_audio(file_path)
        
      
        summary = summarize_text(transcription)
        
       
        timestamps = extract_timestamps(transcription)
        
        
        results_dir = "results"
        os.makedirs(results_dir, exist_ok=True)
        transcription_path = os.path.join(results_dir, f"{file.filename}_transcription.txt")
        summary_path = os.path.join(results_dir, f"{file.filename}_summary.txt")
        timestamps_path = os.path.join(results_dir, f"{file.filename}_timestamps.json")
        
        with open(transcription_path, "w") as f:
            f.write(transcription)
        
        with open(summary_path, "w") as f:
            f.write(summary)
        
        with open(timestamps_path, "w") as f:
            json.dump(timestamps, f)
        
        return JSONResponse(status_code=200, content={
            "transcription": transcription,
            "summary": summary,
            "timestamps": timestamps
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
       
        if os.path.exists(file_path):
            os.remove(file_path)

