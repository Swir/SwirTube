<div align="center">

# 🎬 SwirTube

### Rich-powered terminal media downloader built on `yt-dlp`

**Python • yt-dlp • Rich • FFmpeg • MP3 Extraction • Config • Logs**

![Python](https://img.shields.io/badge/Python-3.x-0D1117?style=for-the-badge&logo=python&logoColor=00A6FF)
![yt-dlp](https://img.shields.io/badge/ENGINE-yt--dlp-0D1117?style=for-the-badge&logo=youtube&logoColor=00A6FF)
![Rich](https://img.shields.io/badge/CLI-Rich-0D1117?style=for-the-badge&logo=gnometerminal&logoColor=00A6FF)
![FFmpeg](https://img.shields.io/badge/AUDIO-FFmpeg-0D1117?style=for-the-badge&logo=ffmpeg&logoColor=00A6FF)

[![Profile](https://img.shields.io/badge/Author-Swir-0088FF?style=flat-square&logo=github)](https://github.com/Swir)
[![Stars](https://img.shields.io/github/stars/Swir/SwirTube?style=flat-square&color=0088FF)](https://github.com/Swir/SwirTube/stargazers)

</div>

---

## 🚀 What is it?

**SwirTube** is a lightweight Python terminal frontend for `yt-dlp`. It combines a cleaner Rich-based interface with local configuration, logging and optional FFmpeg audio extraction.

The goal is simple: keep the flexibility of `yt-dlp`, but make common download workflows quicker and easier to use from a terminal.

---

## ✨ Highlights

| Feature | What it does |
|---|---|
| 🎬 Media download | Process URLs supported by `yt-dlp` |
| 🎵 MP3 extraction | Extract audio using FFmpeg at 192 kb/s |
| 📊 Rich terminal UI | Progress bars, prompts and readable status output |
| ⚙️ FFmpeg path | Use FFmpeg from `PATH` or a configured location |
| 🍪 Cookies file | Optional cookie-file support |
| 💾 Local config | Save preferences to `config.json` |
| 📜 Logging | Store operation details in `downloader.log` |
| 🧩 Lightweight | One main Python script + standard dependencies |

---

## ⚙️ Quick start

### 1. Clone

```bash
git clone https://github.com/Swir/SwirTube.git
cd SwirTube
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
python swirtube.py
```

For audio conversion, install **FFmpeg** and make it available in `PATH` or configure its executable path in the app.

---

## 📋 Requirements

- Python 3.x
- `yt-dlp`
- `rich`
- FFmpeg for audio extraction

---

## 🧩 Project files

```text
SwirTube/
├── swirtube.py
├── requirements.txt
└── README.md
```

`config.json` and `downloader.log` are created locally when the program uses them.

---

## 🔎 Search keywords

`yt-dlp python cli` • `video downloader python` • `yt-dlp frontend` • `yt-dlp mp3` • `rich downloader cli` • `ffmpeg audio extractor` • `terminal media downloader`

---

## ⚖️ Responsible use

Use SwirTube only for media you are authorized to download and in accordance with applicable platform terms and law. The project does not grant rights to third-party content.

---

<div align="center">

### `yt-dlp power with a cleaner terminal workflow`

⭐ **If SwirTube is useful to you, leave a star — it helps the project get discovered.**

[**← Visit SWIR profile**](https://github.com/Swir) · [**Browse all projects →**](https://github.com/Swir?tab=repositories)

</div>
