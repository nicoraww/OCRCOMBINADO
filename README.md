# ocr-audio
# Aplicación de OCR, Traducción y Text-to-Speech

Esta aplicación web combina reconocimiento óptico de caracteres (OCR), traducción y conversión de texto a voz. Permite a los usuarios capturar texto de imágenes, traducirlo a varios idiomas y convertirlo en audio, todo desde una interfaz web intuitiva construida con Streamlit.

## Características Principales

- Captura de texto desde imágenes mediante OCR
- Múltiples fuentes de entrada de imagen:
  - Captura desde cámara web
  - Carga de archivos (PNG, JPG)
- Traducción entre múltiples idiomas:
  - Inglés
  - Español
  - Bengali
  - Coreano
  - Mandarín
  - Japonés
- Conversión de texto a voz con diferentes acentos
- Filtros de imagen para mejorar el reconocimiento OCR
- Interfaz de usuario intuitiva

## Requisitos

```
streamlit
opencv-python (cv2)
numpy
pytesseract
Pillow
gtts
googletrans
```

## Instalación

1. Clone el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. Instale las dependencias:
```bash
pip install -r requirements.txt
```

3. Instale Tesseract OCR:
- Para Ubuntu/Debian:
```bash
sudo apt-get install tesseract-ocr
```
- Para Windows, descargue el instalador de la [página oficial de Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

## Estructura del Proyecto

```
├── app.py
├── temp/
│   └── (archivos de audio temporales)
├── requirements.txt
└── README.md
```

## Uso

1. Inicie la aplicación:
```bash
streamlit run app.py
```

2. Seleccione la fuente de imagen:
   - Active la casilla "Usar Cámara" para utilizar la cámara web
   - O utilice el cargador de archivos para subir una imagen

3. Configure los parámetros de traducción en la barra lateral:
   - Seleccione el idioma de entrada
   - Seleccione el idioma de salida
   - Elija el acento deseado para el audio
   
4. Procese la imagen y genere el audio:
   - El texto reconocido se mostrará en pantalla
   - Presione "convert" para generar el audio
   - Opcionalmente, active "Mostrar texto" para ver la traducción

## Funcionalidades Detalladas

### Procesamiento de Imágenes
- Soporte para imágenes PNG y JPG
- Opción de filtro para mejorar el reconocimiento de texto
- Conversión automática de espacio de color para optimizar el OCR

### Traducción
- Soporte para 6 idiomas principales
- Traducción bidireccional entre cualquier par de idiomas
- Visualización opcional del texto traducido

### Text-to-Speech
- Múltiples acentos disponibles:
  - Default
  - India
  - Reino Unido
  - Estados Unidos
  - Canadá
  - Australia
  - Irlanda
  - Sudáfrica
- Generación automática de archivos de audio
- Reproducción directa en el navegador

## Mantenimiento

La aplicación incluye una función de limpieza automática que elimina los archivos de audio temporales después de 7 días para gestionar el espacio en disco.

```python
remove_files(7)  # Elimina archivos de audio más antiguos que 7 días
```

## Limitaciones

- Requiere conexión a internet para las funciones de traducción y text-to-speech
- La calidad del OCR depende de la calidad de la imagen de entrada
- Algunos idiomas pueden requerir paquetes de idiomas adicionales para Tesseract

## Solución de Problemas

1. Si el OCR no funciona:
   - Verifique la instalación de Tesseract
   - Asegúrese de que la imagen tiene buena calidad y contraste

2. Si la traducción falla:
   - Verifique su conexión a internet
   - Asegúrese de que el texto fue correctamente reconocido

3. Si el audio no se genera:
   - Verifique los permisos de escritura en la carpeta 'temp'
   - Asegúrese de tener conexión a internet

## Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Cree una rama para su función
3. Envíe un Pull Request

## Licencia
CC
