from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from speechace import evaluate_speech, format_speechace_response
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/evaluate")
async def evaluate(
    file: UploadFile = File(...),
    text: str = Form(...),
    language: str = Form("en-us")
):
    try:
        audio_content = await file.read()
        raw_response = evaluate_speech(audio_content, text, language)
        
        if not raw_response:
             raise HTTPException(status_code=500, detail="Failed to get response from SpeechAce")

        formatted_response = format_speechace_response(raw_response)
        return formatted_response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
