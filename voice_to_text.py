import whisper
import numpy as np
import scipy.io.wavfile
import os
# Load Whisper model (base or small for faster inference)
# model = whisper.load_model("base")

# # Transcribe from an audio file (e.g., .mp3 or .wav)
# result = model.transcribe("your_audio_file.wav")

# # Get the text
# text = result["text"]
# print("Transcribed Text:", text)

def transcribe_text(audio):
    sample_rate,audio_np  = audio
    # print(audio)snp,sample_rate)
    temp_path = "temp.wav"
    scipy.io.wavfile.write(temp_path, sample_rate, audio_np)
    model = whisper.load_model("base")
    if audio_np.dtype != np.int16:
        audio_np = (audio_np * 32767).astype(np.int16)

    # Transcribe from an audio file (e.g., .mp3 or .wav)
    result = model.transcribe(temp_path)

    # Get the text
    text = result["text"]
    print("Transcribed Text:", text)
    os.remove(temp_path)
    return text

if __name__ == "__main__":
    transcribe_text()