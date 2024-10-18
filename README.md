# Monitorowanie aktywności komputera z rejestracją naciśnięć klawiszy i powiadomieniami

## Opis

Ten skrypt Python umożliwia monitorowanie aktywności komputera, w tym rejestrowanie uruchomionych aplikacji oraz naciśnięć klawiszy. Działa w tle, zapisując wyniki w plikach logów, które można wysyłać na e-mail. Skrypt można wykorzystać do:

- Monitorowania aktywności dzieci na komputerze.
- Śledzenia wydajności pracowników.
- Lepszego zarządzania własnym czasem spędzonym w aplikacjach.

## Funkcje

### 1. Monitorowanie uruchomionych aplikacji:
- Regularnie sprawdza, które aplikacje są aktywne.
- Rejestruje czas uruchomienia i czas aktywności każdej aplikacji.
- Można zdefiniować listę aplikacji, które mają być monitorowane (np. przeglądarki, edytory tekstu).

### 2. Rejestracja naciśnięć klawiszy (keylogger):
- Rejestruje wszystkie naciśnięcia klawiszy na klawiaturze.
- Wyniki zapisywane są w pliku tekstowym.

### 3. Generowanie raportu z aktywności aplikacji:
- Tworzy plik CSV z listą uruchomionych aplikacji oraz czasem ich aktywności.
- Raport można otworzyć w Excelu lub innym programie do obsługi arkuszy kalkulacyjnych.

### 4. Generowanie wykresu aktywności:
- Tworzy wykres przedstawiający czas spędzony w poszczególnych aplikacjach.

### 5. Powiadomienia o nadmiernym użyciu aplikacji:
- Sprawdza, czy aplikacja była używana przez dłużej niż określony czas (np. 30 minut).
- Wyświetla ostrzeżenie w terminalu, jeśli czas zostanie przekroczony.

### 6. Wysyłanie logów na e-mail:
- Wysyła wiadomość e-mail z załączonymi logami naciśnięć klawiszy i raportem z aktywności aplikacji.
- Wspiera konfigurację wysyłania przez Gmail lub inne serwery pocztowe.

## Użyte technologie

- **Python**: Skrypt został napisany w Pythonie, korzysta z bibliotek:
  - `psutil`: do monitorowania procesów.
  - `pynput`: do rejestrowania naciśnięć klawiszy.
  - `smtplib`: do wysyłania e-maili.
  - `matplotlib`: do generowania wykresów aktywności aplikacji.
  
- **SMTP**: Używany do wysyłania wiadomości e-mail (np. za pomocą serwera Gmail).

## Proces działania

1. **Uruchomienie skryptu**: Skrypt nasłuchuje naciśnięć klawiszy i monitoruje aktywność aplikacji.
2. **Monitorowanie aktywności**: Regularnie sprawdza aktywne aplikacje i rejestruje naciśnięcia klawiszy.
3. **Zapis logów**: Po zakończeniu monitorowania dane są zapisywane w plikach (CSV i tekstowy).
4. **Wizualizacja danych**: Skrypt generuje wykres przedstawiający czas spędzony w aplikacjach.
5. **Wysyłanie e-maila**: Po zakończeniu monitorowania wysyłana jest wiadomość e-mail z załączonymi logami.

## Przykładowa konfiguracja (`config.json`)

```json
{
  "duration_seconds": 3600,
  "alert_threshold": 1800,
  "screenshot_interval": 60,
  "email": {
    "to_email": "odbiorca@example.com"
  }
}

#

 Computer Activity Monitoring with Keylogging and Notifications

## Description

This Python script monitors computer activity, including logging running applications and keystrokes. It works in the background, saving the results in log files, which can be emailed. The script can be used for:

- Monitoring children's computer activity.
- Tracking employee productivity.
- Managing your own time spent in various applications.

## Features

### 1. Monitoring running applications:
- Regularly checks which applications are active.
- Logs the time of launch and total time of activity for each application.
- You can define which applications to monitor (e.g., browsers, text editors).

### 2. Keylogging:
- Logs all keystrokes.
- Stores the results in a text file.

### 3. Application activity report:
- Generates a CSV file listing active applications and their usage times.
- The report can be opened in Excel or other spreadsheet software.

### 4. Activity graph:
- Creates a graph that visualizes the time spent in each application.

### 5. Excessive usage alerts:
- Checks if an application has been used for longer than a defined threshold (e.g., 30 minutes).
- Displays a warning in the terminal if the threshold is exceeded.

### 6. Sending logs via email:
- Sends an email with the keylogging and application activity logs attached.
- Supports Gmail and other email servers through proper configuration.

## Technologies Used

- **Python**: The script is written in Python and uses the following libraries:
  - `psutil`: for process monitoring.
  - `pynput`: for keylogging.
  - `smtplib`: for sending emails.
  - `matplotlib`: for generating application activity graphs.
  
- **SMTP**: Used for sending emails (e.g., through Gmail).

## How It Works

1. **Start the script**: It starts monitoring keypresses and application activity.
2. **Activity monitoring**: It regularly checks which applications are active and logs all keystrokes.
3. **Log saving**: At the end of the monitoring period, data is saved in files (CSV for application activity and a text file for keypresses).
4. **Data visualization**: A graph of the time spent in applications is generated.
5. **Email sending**: The script automatically sends an email with attached logs at the end of the monitoring period.

## Sample configuration (`config.json`)

```json
{
  "duration_seconds": 3600,
  "alert_threshold": 1800,
  "screenshot_interval": 60,
  "email": {
    "to_email": "recipient@example.com"
  }
}
