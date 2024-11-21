# SwirTube

Prosty downloader YouTube napisany w Pythonie, który pozwala na pobieranie filmów lub wyodrębnianie audio w formacie MP3. Program oferuje przyjazny interfejs konsoli z paskami postępu i szczegółowym logowaniem. Dodatkowo umożliwia podanie ścieżki do `ffmpeg`, jeśli nie jest on dostępny w zmiennej środowiskowej `PATH`.

A simple Python-based YouTube downloader that allows you to download videos or extract audio in MP3 format. The program provides a user-friendly console interface with progress bars and detailed logging. It also allows you to specify the path to `ffmpeg` if it's not available in your system's `PATH`.

## Funkcje / Features

- **Pobieranie Filmów z YouTube:** Zapisz filmy w najlepszej dostępnej jakości.
- **Wyodrębnianie Audio:** Konwertuj i zapisuj audio jako pliki MP3.
- **Przyjazny Interfejs:** Interaktywne menu z opcjami pobierania i konfiguracji `ffmpeg`.
- **Paski Postępu:** Paski postępu pokazujące status pobierania.
- **Logowanie:** Szczegółowe logi działań i błędów.
- **Konfiguracja:** Zapisuje ustawienia ścieżki do `ffmpeg` dla przyszłych użyć.

- **Download YouTube Videos:** Save videos in the best available quality.
- **Extract Audio:** Convert and save audio as MP3 files.
- **User-Friendly Interface:** Interactive menu with options for downloading and configuring `ffmpeg`.
- **Progress Indicators:** Progress bars showing download status.
- **Logging:** Detailed logs of activities and errors.
- **Configuration Persistence:** Saves `ffmpeg` path settings for future use.

## Wymagania / Prerequisites

- **Python 3.6+** zainstalowany na Twoim systemie.
- **ffmpeg** zainstalowany i dostępny poprzez `PATH`, lub możliwość ręcznego podania jego lokalizacji.

- **Python 3.6+** installed on your system.
- **ffmpeg** installed and accessible via `PATH`, or the ability to manually specify its location.

## Instalacja / Installation

1. **Sklonuj Repozytorium:**

   ```bash
   git clone https://github.com/yourusername/youtube-downloader.git
   cd youtube-downloader
