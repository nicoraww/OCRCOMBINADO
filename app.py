import os
import time
import glob
import base64

import streamlit as st
from PIL import Image
import cv2
import numpy as np
import pytesseract
from googletrans import Translator
from gtts import gTTS

# Configuración de la página
st.set_page_config(
    page_title="📸 OCR Traductor", 
    page_icon="🖼️", 
    layout="wide"
)

# Estilos y tipografía
st.markdown("""
<style>
  body { background-color: #ffffff; color: #000000; }
  .block-container { padding: 2rem 3rem; background: #f9f9f9; }
  h1, h2, h3, h4, h5 { color: #000000; }
  .stButton > button { color: #000000; border: 1px solid #000000; padding: 0.6rem 1.2rem; font-size: 1rem; }
  a { color: #000000; }
</style>
""", unsafe_allow_html=True)

# Banner
if os.path.exists('ocr_banner.png'):
    st.image('ocr_banner.png', use_column_width=True)

# Título
st.title("🖼️ OCR y Traductor de Texto en Imágenes")

# Selección de fuente de imagen
st.markdown("## 📥 Carga o captura tu imagen")
mode = st.radio("Elige fuente:", ['📷 Cámara', '📁 Cargar archivo'], index=1, horizontal=True)

if mode == '📷 Cámara':
    img_buffer = st.camera_input("Toma una foto:")
else:
    img_buffer = st.file_uploader("Selecciona un archivo PNG/JPG:", type=['png','jpg'])

# Mostrar y procesar imagen
if img_buffer:
    file_bytes = img_buffer.getvalue()
    nparr = np.frombuffer(file_bytes, np.uint8)
    img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    st.image(img_cv, caption='🔍 Vista previa', use_column_width=True)

    # OCR
    st.markdown("## 🔎 Reconociendo texto...")
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    extracted = pytesseract.image_to_string(img_rgb)
    st.success("✅ Texto extraído:")
    st.code(extracted, language='text')
else:
    extracted = ""

# Sidebar: parámetros de traducción y audio
with st.sidebar:
    st.header("🌐 Configuración de Traducción")
    LANGS = {
        '🇪🇸 Español': 'es', '🇬🇧 English': 'en', '🇨🇳 中文': 'zh-cn',
        '🇰🇷 한국어': 'ko', '🇯🇵 日本語': 'ja', '🇧🇩 বাংলা': 'bn'
    }
    src_key = st.selectbox('🔄Idioma origen', list(LANGS.keys()), index=0)
    dst_key = st.selectbox('🔁Idioma destino', list(LANGS.keys()), index=1)
    accent = st.selectbox('📣 Acento (TLD)',['com','co.uk','com.au','ca','ie','co.za'], index=0)
    play = st.button('🎧 Traducir y generar audio')
    remove_days = st.slider('🗑️Eliminar audios con más de días:', 1, 30, 7)

# Función de texto a audio
def text_to_speech(text, src, dst, tld):
    translator = Translator()
    translated = translator.translate(text, src=src, dest=dst).text
    tts = gTTS(translated, lang=dst, tld=tld, slow=False)
    os.makedirs('temp', exist_ok=True)
    fname = f"ocr_{int(time.time())}.mp3"
    path = os.path.join('temp', fname)
    tts.save(path)
    return translated, path

# Al pulsar el botón
def handle_audio():
    if extracted.strip() == "":
        st.warning("📋 No hay texto para traducir.")
        return
    translated, audio_file = text_to_speech(
        extracted,
        src=LANGS[src_key],
        dst=LANGS[dst_key],
        tld=accent
    )
    st.balloons()
    st.markdown("## 📜 Texto traducido:")
    st.write(translated)
    audio_bytes = open(audio_file, 'rb').read()
    st.audio(audio_bytes)
    b64 = base64.b64encode(audio_bytes).decode()
    dl = f"<a href='data:audio/mp3;base64,{b64}' download='{os.path.basename(audio_file)}'>⬇️ Descargar audio</a>"
    st.markdown(dl, unsafe_allow_html=True)

if play:
    handle_audio()

# Limpieza de archivos antiguos
def cleanup(days):
    cutoff = time.time() - days * 86400
    for f in glob.glob('temp/*.mp3'):
        if os.stat(f).st_mtime < cutoff:
            os.remove(f)

cleanup(remove_days)
