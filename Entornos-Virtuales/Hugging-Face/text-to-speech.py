from transformers import pipeline
import scipy.io.wavfile
import numpy as np

# Crea el sintetizador con Bark
synthesiser = pipeline("text-to-speech", model="suno/bark")

# Genera el audio
speech = synthesiser(
    "Hello, I'm trying suno bark text to speech",
    forward_params={"do_sample": True}
)

# Extrae y normaliza el audio
audio = speech["audio"].flatten()  # <- aplanar el array
if audio.dtype != np.int16:
    audio = np.int16(audio / np.max(np.abs(audio)) * 32767)

# Guarda el WAV
rate = int(speech["sampling_rate"])
scipy.io.wavfile.write("bark_out.wav", rate, audio)

print("Archivo guardado como bark_out.wav")