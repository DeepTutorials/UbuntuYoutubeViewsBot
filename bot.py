import webbrowser
import time
import subprocess

def open_url_in_firefox(url, duration=60):
    """
    Öffnet eine URL im Firefox-Browser und misst die Verweilzeit.
    
    :param url: Die zu öffnende URL.
    :param duration: Maximale Zeit in Sekunden, während Firefox überwacht wird.
    """
    # Zählt, wie oft die URL geöffnet wird
    open_count = 0

    # Startzeit
    start_time = time.time()
    print(f"Öffne {url} im Firefox-Browser...")

    # Öffne die URL im Firefox-Browser
    webbrowser.get("firefox").open(url)
    open_count += 1
    print("Firefox wurde geöffnet.")

    while True:
        # Überwachungsschleife: Überprüfe, ob Firefox noch läuft
        try:
            result = subprocess.run(
                ["pgrep", "firefox"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )

            if result.stdout.strip():
                print("Firefox läuft...")
            else:
                print("Firefox wurde geschlossen.")
                break

            # Abbruchbedingung basierend auf Zeit
            if time.time() - start_time > duration:
                print("Zeitlimit erreicht. Beende Überwachung.")
                break

            time.sleep(5)  # Wartezeit vor dem nächsten Check
        except KeyboardInterrupt:
            print("\nAbbruch durch Benutzer.")
            break

    total_time = time.time() - start_time
    print(f"Firefox war insgesamt {total_time:.2f} Sekunden geöffnet.")
    print(f"Die URL wurde insgesamt {open_count} mal geöffnet.")

# URL zum Öffnen
url_to_open = "https://www.example.com"

# Skript ausführen
open_url_in_firefox(url_to_open, duration=60)
