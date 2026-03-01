from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import azure.cognitiveservices.speech as speechsdk
import os
from dotenv import load_dotenv
import io

load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextChunkRequest(BaseModel):
    text: str

@app.post("/speak-chunk")
async def speak_chunk(request: TextChunkRequest):

    speech_config = speechsdk.SpeechConfig(
        subscription=SPEECH_KEY,
        region=SPEECH_REGION
    )

    speech_config.speech_synthesis_voice_name = "hi-IN-SwaraNeural"

    speech_config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Audio16Khz32KBitRateMonoMp3
    )

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=None
    )

    # result = synthesizer.speak_text_async(request.text).get()
    ssml = f"""
    <speak version='1.0' xml:lang='hi-IN'>
      <voice name='hi-IN-SwaraNeural'>
        <prosody rate='+25%'>
          {request.text}
        </prosody>
      </voice>
    </speak>
    """

    result = synthesizer.speak_ssml_async(ssml).get()

    if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        return {"error": "Speech synthesis failed"}

    return StreamingResponse(
        io.BytesIO(result.audio_data),
        media_type="audio/mpeg"
    )