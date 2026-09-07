<div align="center">

# 🎬 SwirTube

**Terminal YouTube video & audio downloader powered by yt-dlp**  
**Terminalowy downloader wideo i audio z YouTube oparty na yt-dlp**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![yt-dlp](https://img.shields.io/badge/Engine-yt--dlp-red)
![CLI](https://img.shields.io/badge/UI-Rich-8A2BE2)
![FFmpeg](https://img.shields.io/badge/Audio-FFmpeg-007808?logo=ffmpeg)

</div>

---

## 🇵🇱 Polski

SwirTube to terminalowy downloader napisany w Pythonie. Program wykorzystuje `yt-dlp` do pobierania materiałów, `Rich` do czytelnego interfejsu konsolowego oraz FFmpeg do konwersji ścieżek audio do MP3.

### ✨ Funkcje
- pobieranie wideo z pojedynczego URL
- ekstrakcja audio do MP3 192 kb/s
- obsługa własnej ścieżki do FFmpeg
- opcjonalny plik cookies
- zapis ustawień do `config.json`
- logowanie działania do `downloader.log`
- paski postępu i komunikaty przez bibliotekę Rich

### 🚀 Instalacja

```bash
git clone https://github.com/Swir/SwirTube.git
cd SwirTube
pip install yt-dlp rich
python swirtube.py
```

Do konwersji audio wymagany jest **FFmpeg** dostępny w `PATH` albo wskazany w konfiguracji programu.

---

## 🇬🇧 English

SwirTube is a Python terminal downloader built around `yt-dlp`. It uses `Rich` for a clean console interface and FFmpeg for audio post-processing and MP3 extraction.

### ✨ Features
- download video from a single URL
- extract audio to 192 kb/s MP3
- configurable FFmpeg location
- optional cookies file
- persistent settings in `config.json`
- operation logs in `downloader.log`
- Rich progress bars and terminal prompts

### 🚀 Installation

```bash
git clone https://github.com/Swir/SwirTube.git
cd SwirTube
pip install yt-dlp rich
python swirtube.py
```

Audio conversion requires **FFmpeg** in your system `PATH` or configured directly in the application.

---

## ⚖️ Responsible use / Odpowiedzialne użycie
Use SwirTube only for media you are authorized to download and in accordance with the source platform's terms.  
Korzystaj z programu wyłącznie do materiałów, które masz prawo pobierać, zgodnie z zasadami platformy źródłowej.

## 👤 Author / Autor
Developed by **Swir**.
