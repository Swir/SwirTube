# SwirTube - YouTube Downloader

![🇵🇱 Polski](https://img.shields.io/badge/Language-Polski-blue) ![🇬🇧 English](https://img.shields.io/badge/Language-English-green)

---

## 🇵🇱 Opis Projektu

**SwirTube** to nowoczesny i intuicyjny program do pobierania wideo oraz audio z YouTube. Wykorzystuje bibliotekę `yt_dlp` oraz `Rich` do tworzenia przyjaznego interfejsu w terminalu.

### 📋 Funkcje

- **Pobieranie wideo** w wybranej jakości (MP4/WebM)
- **Pobieranie audio** w formacie MP3
- **Dynamiczny wybór dostępnych jakości wideo**
- **Obsługa plików cookies** dla uwierzytelnionego pobierania
- **Konfiguracja ścieżki do `ffmpeg`**
- **Łatwe w użyciu menu** z intuicyjnymi opcjami

### 🍪 Obsługa Plików Cookies

**SwirTube** umożliwia korzystanie z plików cookies (`cookies.txt`), co pozwala na uwierzytelnione pobieranie treści chronionych lub dostępnych tylko dla zalogowanych użytkowników. 

#### Jak Utworzyć `cookies.txt`:

1. **Zaloguj się na YouTube:**
   - Otwórz przeglądarkę i zaloguj się na swoje konto YouTube.

2. **Zainstaluj Rozszerzenie do Eksportowania Cookies:**
   - Na przykład, możesz użyć [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/llfapgnmjlpndacddaoapfljgddadacj) dla Google Chrome.

3. **Eksportuj Pliki Cookies:**
   - Po zainstalowaniu rozszerzenia, kliknij jego ikonę w przeglądarce.
   - Wybierz domenę `youtube.com` i wyeksportuj pliki cookies do pliku `cookies.txt`.

4. **Umieść `cookies.txt` w Katalogu Programu:**
   - Skopiuj plik `cookies.txt` do folderu, w którym znajduje się `downloader.py`.

#### Używanie Plików Cookies w Programie:

- **Automatyczne Wykrywanie:**
  - Program automatycznie sprawdza, czy plik `cookies.txt` istnieje w katalogu. Jeśli tak, używa go do uwierzytelnionego pobierania.
  
- **Brak Pliku Cookies:**
  - Jeśli `cookies.txt` nie zostanie znaleziony, program będzie próbował pobrać treści bez użycia cookies.

### 🛠 Instalacja

1. **Klonowanie Repozytorium:**

    ```bash
    git clone https://github.com/Swir/SwirTube.git
    cd SwirTube
    ```

2. **Instalacja Wymagań:**

    Upewnij się, że masz zainstalowanego Pythona (wersja 3.6 lub wyższa).

    ```bash
    pip install -r requirements.txt
    ```

3. **Instalacja `ffmpeg`:**

    Pobierz i zainstaluj `ffmpeg` z [oficjalnej strony](https://ffmpeg.org/download.html). Dodaj `ffmpeg` do zmiennej środowiskowej PATH lub skonfiguruj ścieżkę w programie.

### 🎬 Użycie

1. **Uruchomienie Programu:**

    ```bash
    python downloader.py
    ```

2. **Kroki w Programie:**
    - Wybierz opcję pobierania z YouTube.
    - Podaj URL wideo.
    - Wybierz format pobierania (wideo/audio).
    - Wybierz jakość wideo (jeśli wybrano wideo).
    - Wybierz format kontenera (MP4/WebM).
    - Rozpocznij pobieranie.

### ⚙️ Konfiguracja

- **Ustawienie Ścieżki do `ffmpeg`:**

    Jeśli `ffmpeg` nie jest w PATH, wybierz opcję ustawienia ścieżki w menu programu i podaj pełną ścieżkę do pliku `ffmpeg.exe`.

### 🤝 Wkład w Projekt

1. Forkuj repozytorium.
2. Stwórz swoją gałąź (`git checkout -b feature/NazwaFunkcji`).
3. Zatwierdź zmiany (`git commit -m 'Dodaj nową funkcję'`).
4. Pushuj do gałęzi (`git push origin feature/NazwaFunkcji`).
5. Otwórz Pull Request.

### 📄 Licencja

Ten projekt jest objęty licencją MIT. Zobacz plik [LICENSE](LICENSE) po więcej informacji.

---

## 🇬🇧 Project Description

**SwirTube** is a modern and intuitive program for downloading videos and audio from YouTube. It leverages the `yt_dlp` and `Rich` libraries to create a user-friendly terminal interface.

### 📋 Features

- **Download videos** in selected quality (MP4/WebM)
- **Download audio** in MP3 format
- **Dynamic selection of available video qualities**
- **Support for cookies** for authenticated downloads
- **Configuration of `ffmpeg` path**
- **Easy-to-use menu** with intuitive options

### 🍪 Cookies Support

**SwirTube** allows the use of cookies (`cookies.txt`), enabling authenticated downloads of protected content or content available only to logged-in users.

#### How to Create `cookies.txt`:

1. **Log in to YouTube:**
   - Open your browser and log in to your YouTube account.

2. **Install a Cookie Export Extension:**
   - For example, use [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/llfapgnmjlpndacddaoapfljgddadacj) for Google Chrome.

3. **Export Cookies:**
   - After installing the extension, click its icon in the browser.
   - Select the `youtube.com` domain and export the cookies to a `cookies.txt` file.

4. **Place `cookies.txt` in the Program Directory:**
   - Copy the `cookies.txt` file to the folder where `downloader.py` is located.

#### Using Cookies in the Program:

- **Automatic Detection:**
  - The program automatically checks if `cookies.txt` exists in the directory. If found, it uses it for authenticated downloads.
  
- **No Cookies File:**
  - If `cookies.txt` is not found, the program will attempt to download content without using cookies.

### 🛠 Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Swir/SwirTube.git
    cd SwirTube
    ```

2. **Install Requirements:**

    Ensure you have Python installed (version 3.6 or higher).

    ```bash
    pip install -r requirements.txt
    ```

3. **Install `ffmpeg`:**

    Download and install `ffmpeg` from the [official website](https://ffmpeg.org/download.html). Add `ffmpeg` to your system PATH or configure the path within the program.

### 🎬 Usage

1. **Run the Program:**

    ```bash
    python downloader.py
    ```

2. **Program Steps:**
    - Select the option to download from YouTube.
    - Enter the video URL.
    - Choose the download format (video/audio).
    - Select the video quality (if video is chosen).
    - Choose the container format (MP4/WebM).
    - Start the download.

### ⚙️ Configuration

- **Setting the `ffmpeg` Path:**

    If `ffmpeg` is not in PATH, select the option to set the path in the program menu and provide the full path to the `ffmpeg.exe` file.

### 🤝 Contributing

1. Fork the repository.
2. Create your branch (`git checkout -b feature/FeatureName`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/FeatureName`).
5. Open a Pull Request.

### 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 📷 Screenshots

### 🇵🇱 Polska

![Menu](screenshots/menu_pl.png)

### 🇬🇧 English

![Menu](screenshots/menu_en.png)


## 🔗 Linki

- [Repozytorium GitHub](https://github.com/Swir/SwirTube)
- [Strona Projektu](https://github.com/Swir/SwirTube)
