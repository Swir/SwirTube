import os
import sys
import logging
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, DownloadColumn
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
import subprocess
import json

# Konfiguracja logowania
logging.basicConfig(
    filename='downloader.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Inicjalizacja konsoli Rich
console = Console()

# Plik konfiguracyjny
CONFIG_FILE = 'config.json'

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            console.print("[red]Błąd wczytywania pliku konfiguracyjnego. Używanie domyślnych ustawień.[/red]")
            return {}
    return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

class YDLLogger:
    def debug(self, msg):
        logging.debug(msg)

    def warning(self, msg):
        logging.warning(msg)
        console.print(f"[yellow]{msg}[/yellow]")

    def error(self, msg):
        logging.error(msg)
        console.print(f"[red]{msg}[/red]")

def check_ffmpeg(ffmpeg_path=None):
    try:
        if ffmpeg_path:
            subprocess.run([ffmpeg_path, '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            subprocess.run(['ffmpeg', '-version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception:
        return False

class Downloader:
    def __init__(self, url, format_choice, cookies=None, ffmpeg_location=None):
        """
        Inicjalizacja Downloadera.

        :param url: URL wideo do pobrania z YouTube
        :param format_choice: Wybrany format ('video' lub 'audio')
        :param cookies: Ścieżka do pliku cookie (opcjonalnie)
        :param ffmpeg_location: Ścieżka do ffmpeg (opcjonalnie)
        """
        self.url = url
        self.format_choice = format_choice
        self.cookies = cookies
        self.ffmpeg_location = ffmpeg_location

    def download(self):
        """
        Metoda główna do pobierania wideo lub audio z YouTube.
        """
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(os.getcwd(), '%(title)s.%(ext)s'),
                'noplaylist': True,
                'quiet': True,
                'no_warnings': True,
                'logger': YDLLogger(),
            }

            if self.format_choice == 'audio':
                ydl_opts.update({
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'postprocessor_args': [
                        '-ar', '16000'
                    ],
                    'prefer_ffmpeg': True,
                })

            if self.ffmpeg_location:
                ydl_opts['ffmpeg_location'] = self.ffmpeg_location

            if self.cookies:
                ydl_opts['cookiefile'] = self.cookies

            console.print(f"[green]Pobieranie z YouTube:[/green] {self.url}")

            with Progress(
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                DownloadColumn(),
                TimeRemainingColumn(),
                console=console,
                transient=True,
            ) as progress:
                task_id = progress.add_task("[cyan]Pobieranie...", total=0)

                def ydl_hook(d):
                    if d['status'] == 'downloading':
                        downloaded = d.get('downloaded_bytes', 0)
                        total = d.get('total_bytes', 0) or d.get('total_bytes_estimate', 0)
                        if total and not progress.tasks[task_id].total:
                            progress.update(task_id, total=total)
                        progress.update(task_id, completed=downloaded)
                    elif d['status'] == 'finished':
                        progress.update(task_id, completed=progress.tasks[task_id].total)

                ydl_opts['progress_hooks'] = [ydl_hook]

                with YoutubeDL(ydl_opts) as ydl:
                    ydl.download([self.url])

            logging.info(f"Pobrano z YouTube: {self.url}")
            console.print(f"[green]Pobrano z YouTube: {self.url}[/green]")

        except DownloadError as e:
            logging.error(f"Błąd podczas pobierania z YouTube: {e}")
            console.print(f"[red]Błąd podczas pobierania z YouTube: {e}[/red]")
        except Exception as e:
            logging.error(f"Niespodziewany błąd podczas pobierania z YouTube: {e}")
            console.print(f"[red]Niespodziewany błąd podczas pobierania z YouTube: {e}[/red]")

def set_ffmpeg_path(config):
    """
    Funkcja umożliwiająca ustawienie ścieżki do ffmpeg przez użytkownika.
    """
    console.print("[blue]Ustaw ścieżkę do ffmpeg.[/blue]")
    ffmpeg_path = Prompt.ask("Podaj pełną ścieżkę do pliku ffmpeg (np. C:\\ffmpeg\\bin\\ffmpeg.exe)", default="")
    if ffmpeg_path:
        if os.path.isfile(ffmpeg_path):
            if check_ffmpeg(ffmpeg_path):
                console.print(f"[green]Ścieżka do ffmpeg ustawiona na: {ffmpeg_path}[/green]")
                config['ffmpeg_path'] = ffmpeg_path
                save_config(config)
                return ffmpeg_path
            else:
                console.print("[red]ffmpeg nie działa poprawnie pod podaną ścieżką.[/red]")
                return None
        else:
            console.print("[red]Podana ścieżka nie istnieje lub nie jest plikiem ffmpeg.exe.[/red]")
            return None
    else:
        console.print("[yellow]Nie podano ścieżki do ffmpeg. Program będzie próbował użyć ffmpeg z PATH.[/yellow]")
        config.pop('ffmpeg_path', None)
        save_config(config)
        return None

def main():
    config = load_config()
    ffmpeg_path = config.get('ffmpeg_path', None)

    while True:
        # Wyświetlenie menu
        console.print(Panel("SwirTube - YouTube downloader", subtitle="Wybierz opcję", style="bold blue"))
        console.print("1. Pobierz z YouTube")
        console.print("2. Ustaw ścieżkę do ffmpeg")
        console.print("3. Wyjście")

        choice = Prompt.ask("Wprowadź numer opcji", choices=["1", "2", "3"])

        if choice == "1":
            url = Prompt.ask("Podaj URL wideo z YouTube")
            if not url.startswith("http"):
                console.print("[red]Nieprawidłowy URL. Proszę podać poprawny URL z YouTube.[/red]")
                continue

            # Wybór formatu pobierania
            console.print("\nWybierz format pobierania:")
            console.print("1. Wideo")
            console.print("2. Audio (MP3)")
            format_choice = Prompt.ask("Wprowadź numer opcji", choices=["1", "2"])

            if format_choice == "1":
                selected_format = 'video'
            else:
                selected_format = 'audio'

            # Sprawdzenie istnienia pliku cookies.txt
            cookies_path = 'cookies.txt' if os.path.exists('cookies.txt') else None
            if cookies_path:
                console.print("[blue]Plik cookies.txt został wykryty i będzie użyty.[/blue]")
            else:
                console.print("[blue]Nie znaleziono pliku cookies.txt. Pobieranie bez pliku cookie.[/blue]")

            # Jeśli wybrano audio, sprawdź ffmpeg
            if selected_format == 'audio':
                current_ffmpeg_path = config.get('ffmpeg_path', None)
                if not check_ffmpeg(current_ffmpeg_path):
                    console.print("[red]ffmpeg nie został znaleziony w PATH lub podanej ścieżce.[/red]")
                    if Confirm.ask("Czy chcesz podać ścieżkę do ffmpeg ręcznie?", default=True):
                        ffmpeg_path = set_ffmpeg_path(config)
                        if not ffmpeg_path:
                            console.print("[red]ffmpeg jest wymagany do pobrania audio. Skakanie do głównego menu.[/red]")
                            continue
                    else:
                        console.print("[red]ffmpeg jest wymagany do pobrania audio. Skakanie do głównego menu.[/red]")
                        continue
                else:
                    ffmpeg_path = config.get('ffmpeg_path', None)  # Może być None, jeśli ffmpeg jest w PATH

            downloader = Downloader(url=url, format_choice=selected_format, cookies=cookies_path, ffmpeg_location=ffmpeg_path)
            downloader.download()

        elif choice == "2":
            ffmpeg_path = set_ffmpeg_path(config)
            if ffmpeg_path:
                console.print("[green]Ścieżka do ffmpeg została zaktualizowana.[/green]")
            else:
                console.print("[red]Nie udało się ustawić ścieżki do ffmpeg.[/red]")

        elif choice == "3":
            console.print("[bold green]Dziękujemy za skorzystanie z programu. Do zobaczenia![/bold green]")
            sys.exit(0)

        # Zapytanie, czy użytkownik chce kontynuować
        console.print("\n[blue]Czy chcesz wykonać kolejną operację?[/blue]")
        continue_choice = Confirm.ask("Czy chcesz kontynuować?", default=True)
        if not continue_choice:
            console.print("[bold green]Dziękujemy za skorzystanie z programu. Do zobaczenia![/bold green]")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[red]Pobieranie zostało przerwane przez użytkownika.[/red]")
        logging.info("Pobieranie zostało przerwane przez użytkownika.")
    except Exception as e:
        console.print(f"[red]Niespodziewany błąd: {e}[/red]")
        logging.error(f"Niespodziewany błąd: {e}")
