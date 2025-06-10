import os
import subprocess

def fix_png_profiles(start_dir="Sprites"):
    """
    Przetwarza wszystkie pliki PNG w podanym katalogu startowym i jego podfolderach,
    usuwając profile kolorów iCCP za pomocą ImageMagick's mogrify.
    Wymaga zainstalowanego ImageMagick (komenda 'mogrify' musi być dostępna w PATH).
    """
    print(f"Rozpoczynam przeszukiwanie folderu '{start_dir}' w poszukiwaniu plików PNG...")

    # Sprawdź, czy folder startowy istnieje
    if not os.path.isdir(start_dir):
        print(f"Błąd: Folder '{start_dir}' nie istnieje. Upewnij się, że jest w tej samej lokalizacji co skrypt.")
        return

    # Iteruj przez wszystkie pliki i foldery w podanym katalogu startowym
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.lower().endswith(".png"):
                file_path = os.path.join(root, file)
                print(f"Przetwarzanie pliku: {file_path}")
                try:
                    # Użyj mogrify -strip, aby usunąć wszystkie metadane (w tym profile iCCP)
                    subprocess.run(["magick", "mogrify", "-strip", file_path], check=True, capture_output=True)
                    print(f"   -> Pomyślnie przetworzono.")
                except FileNotFoundError:
                    print("\nBłąd: Nie znaleziono komendy 'mogrify'.")
                    print("Upewnij się, że masz zainstalowany ImageMagick i jest on dodany do zmiennej PATH.")
                    print("Instrukcje instalacji ImageMagick znajdziesz np. na: https://imagemagick.org/script/download.php")
                    return
                except subprocess.CalledProcessError as e:
                    print(f"   -> Błąd podczas przetwarzania pliku {file_path}:")
                    print(f"      Stdout: {e.stdout.decode()}")
                    print(f"      Stderr: {e.stderr.decode()}")
                except Exception as e:
                    print(f"   -> Wystąpił nieoczekiwany błąd podczas przetwarzania {file_path}: {e}")

    print("\nProces zakończony.")
    print("Wszystkie pliki PNG w folderze 'Sprites' i jego podfolderach zostały przetworzone.")
    print("Teraz powinny ładować się w Pygame bez ostrzeżenia 'libpng warning: iCCP: known incorrect sRGB profile'.")

if __name__ == "__main__":
    # Pamiętaj, aby ZROBIĆ KOPIĘ ZAPASOWĄ folderu 'Sprites' przed uruchomieniem skryptu!
    # Ten skrypt MODYFIKUJE oryginalne pliki.
    print("--- OSTRZEŻENIE ---")
    print("Ten skrypt MODYFIKUJE oryginalne pliki PNG w folderze 'Sprites' i jego podfolderach.")
    print("ZALECAM WYKONANIE KOPII ZAPASOWEJ FOLDERU 'Sprites' PRZED URUCHOMIENIEM TEGO SKRYPTU.")
    input("Naciśnij ENTER, aby kontynuować, lub CTRL+C, aby anulować...")
    print("-------------------")

    fix_png_profiles(start_dir="Sprites")