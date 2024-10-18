# Monitorowanie aktywności komputera z rejestracją naciśnięć klawiszy i powiadomieniami / Computer Activity Monitoring with Keylogging and Notifications

## Opis / Description

Ten skrypt Python umożliwia monitorowanie aktywności komputera, w tym rejestrowanie uruchomionych aplikacji oraz naciśnięć klawiszy. Działa w tle, zapisując wyniki w plikach logów, które można wysyłać na e-mail. Skrypt można wykorzystać do:

This Python script monitors computer activity, including logging running applications and keystrokes. It works in the background, saving the results in log files, which can be emailed. The script can be used for:

- Monitorowania aktywności dzieci na komputerze. / Monitoring children's computer activity.
- Śledzenia wydajności pracowników. / Tracking employee productivity.
- Lepszego zarządzania własnym czasem spędzonym w aplikacjach. / Managing your own time spent in various applications.

## Funkcje / Features

### 1. Monitorowanie uruchomionych aplikacji / Monitoring running applications:
- Regularnie sprawdza, które aplikacje są aktywne. / Regularly checks which applications are active.
- Rejestruje czas uruchomienia i czas aktywności każdej aplikacji. / Logs the time of launch and total time of activity for each application.
- Można zdefiniować listę aplikacji, które mają być monitorowane (np. przeglądarki, edytory tekstu). / You can define which applications to monitor (e.g., browsers, text editors).

### 2. Rejestracja naciśnięć klawiszy (keylogger) / Keylogging:
- Rejestruje wszystkie naciśnięcia klawiszy na klawiaturze. / Logs all keystrokes.
- Wyniki zapisywane są w pliku tekstowym. / Stores the results in a text file.

### 3. Generowanie raportu z aktywności aplikacji / Application activity report:
- Tworzy plik CSV z listą uruchomionych aplikacji oraz czasem ich aktywności. / Generates a CSV file listing active applications and their usage times.
- Raport można otworzyć w Excelu lub innym programie do obsługi arkuszy kalkulacyjnych. / The report can be opened in Excel or other spreadsheet software.

### 4. Generowanie wykresu aktywności / Activity graph:
- Tworzy wykres przedstawiający czas spędzony w poszczególnych aplikacjach. / Creates a graph that visualizes the time spent in each application.

### 5. Powiadomienia o nadmiernym użyciu aplikacji / Excessive usage alerts:
- Sprawdza, czy aplikacja była używana przez dłużej niż określony czas (np. 30 minut). / Checks if an application has been used for longer than a defined threshold (e.g., 30 minutes).
- Wyświetla ostrzeżenie w terminalu, jeśli czas zostanie przekroczony. / Displays a warning in the terminal if the threshold is exceeded.

### 6. Wysyłanie logów na e-mail / Sending logs via email:
- Wysyła wiadomość e-mail z załączonymi logami naciśnięć klawiszy i raportem z aktywności aplikacji. / Sends an email with the keylogging and application activity logs attached.
- Wspiera konfigurację wysyłania przez Gmail lub inne serwery pocztowe. / Supports Gmail and other email servers through proper configuration.

## Użyte technologie / Technologies Used

- **Python**: Skrypt został napisany w Pythonie i korzysta z kilku popularnych bibliotek:
  - `psutil`: do monitorowania procesów. / for process monitoring.
  - `pynput`: do rejestrowania naciśnięć klawiszy. / for keylogging.
  - `smtplib`: do wysyłania e-maili. / for sending emails.
  - `matplotlib`: do generowania wykresów aktywności aplikacji. / for generating application activity graphs.
  
- **SMTP**: Używany do wysyłania wiadomości e-mail (np. za pomocą serwera Gmail). / Used for sending emails (e.g., through Gmail).

## Proces działania / How It Works

1. **Uruchomienie skryptu**: Skrypt nasłuchuje naciśnięć klawiszy i monitoruje aktywność aplikacji. / Start the script: It starts monitoring keypresses and application activity.
2. **Monitorowanie aktywności**: Regularnie sprawdza aktywne aplikacje i rejestruje wszystkie naciśnięcia klawiszy. / Activity monitoring: It regularly checks which applications are active and logs all keystrokes.
3. **Zapis logów**: Po zakończeniu monitorowania dane są zapisywane w plikach (CSV dla aktywności aplikacji i tekstowy dla naciśnięć klawiszy). / Log saving: At the end of the monitoring period, data is saved in files (CSV for application activity and a text file for keypresses).
4. **Wizualizacja danych**: Skrypt generuje wykres przedstawiający czas spędzony w aplikacjach. / Data visualization: A graph of the time spent in applications is generated.
5. **Wysyłanie e-maila**: Skrypt automatycznie wysyła wiadomość e-mail z załączonymi logami na koniec monitorowania. / Email sending: The script automatically sends an email with attached logs at the end of the monitoring period.

## Przykładowa konfiguracja (`config.json`) / Sample configuration (`config.json`)

```json
{
  "duration_seconds": 3600,
  "alert_threshold": 1800,
  "screenshot_interval": 60,
  "email": {
    "to_email": "recipient@example.com"
  }
}
