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
##Opis Opcji / Options Description:

    1. Pobierz z YouTube / Download from YouTube:
        Wprowadź URL wideo z YouTube.
        Wybierz format pobierania:
            1. Wideo / Video: Pobierz wideo w najlepszej dostępnej jakości.
            2. Audio (MP3) / Audio (MP3): Wyodrębnij i pobierz audio jako plik MP3.
        Jeśli wybrano audio, program sprawdzi obecność ffmpeg. Jeśli nie jest znaleziony, zapyta o podanie ścieżki ręcznie.

    2. Ustaw ścieżkę do ffmpeg / Set ffmpeg path:
        Podaj pełną ścieżkę do pliku ffmpeg (np. C:\ffmpeg\bin\ffmpeg.exe na Windows lub /usr/local/bin/ffmpeg na macOS/Linux).
        Program sprawdzi poprawność ścieżki i zapisze ją w konfiguracji.

    3. Wyjście / Exit:
        Zakończenie programu.
       
## konf
Program zapisuje ustawienia ścieżki do ffmpeg w pliku config.json, dzięki czemu nie musisz podawać jej przy każdym uruchomieniu programu.

The program saves the ffmpeg path settings in the config.json file, so you don't need to provide it every time you run the program.
Logowanie / Logging

Program zapisuje logi w pliku downloader.log, które zawierają informacje o pobieraniach oraz ewentualnych błędach.

The program logs activities and errors in the downloader.log file.
Wkład / Contributing

Jeśli chcesz przyczynić się do rozwoju tego projektu, otwórz pull request lub zgłoś issue.

If you want to contribute to the development of this project, open a pull request or report an issue.     

##Zainstaluj ffmpeg / Install ffmpeg:
        Windows:
        Pobierz najnowszą statyczną wersję ze strony ffmpeg.
        Rozpakuj zawartość i umieść plik wykonywalny ffmpeg.exe w folderze (np. C:\ffmpeg\bin).
        Dodaj katalog ffmpeg\bin do zmiennej środowiskowej PATH.
        
