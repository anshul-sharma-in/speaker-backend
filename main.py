from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import os
import io

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://stories.anshulsharma.net"
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextChunkRequest(BaseModel):
    text: str

@app.post("/speak-chunk")
async def speak_chunk(request: TextChunkRequest):

    token_url = f"https://{SPEECH_REGION}.api.cognitive.microsoft.com/sts/v1.0/issuetoken"

    token_response = requests.post(
        token_url,
        headers={
            "Ocp-Apim-Subscription-Key": SPEECH_KEY
        }
    )

    access_token = token_response.text

    tts_url = f"https://{SPEECH_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"

    ssml = f"""
    <speak version='1.0' xml:lang='hi-IN'>
        <voice name='hi-IN-SwaraNeural'>
            <prosody rate='+25%'>
                {request.text}
            </prosody>
        </voice>
    </speak>
    """

    response = requests.post(
        tts_url,
        headers={
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3",
            "User-Agent": "speaker-backend"
        },
        data=ssml.encode("utf-8")
    )

    return StreamingResponse(
        io.BytesIO(response.content),
        media_type="audio/mpeg"
    )