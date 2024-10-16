import psutil
import time
import csv
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import matplotlib.pyplot as plt
from collections import defaultdict
from PIL import ImageGrab
import logging
from dotenv import load_dotenv
import json

# Wczytanie konfiguracji z pliku .env
load_dotenv()

# Konfiguracja logowania błędów
logging.basicConfig(filename='errors.log', level=logging.ERROR, 
                    format='%(asctime)s %(levelname)s %(message)s')

# Funkcja do wczytywania konfiguracji z pliku JSON
def load_config(filename="config.json"):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Plik konfiguracyjny config.json nie został znaleziony.")
        return {}

# Wczytanie konfiguracji
config = load_config()
duration_seconds = config.get('duration_seconds', 3600)  # czas między kolejnymi cyklami monitorowania
alert_threshold = config.get('alert_threshold', 1800)  # próg ostrzeżenia o nadmiernym użyciu aplikacji
screenshot_interval = config.get('screenshot_interval', 60)  # interwał robienia zrzutów ekranu w sekundach
email_settings = config.get('email', {})

from_email = os.getenv('EMAIL_USER')
from_password = os.getenv('EMAIL_PASS')

# Definiujemy aplikacje, które chcemy monitorować, wczytując z pliku
def load_monitored_apps(filename="monitored_apps.txt"):
    try:
        with open(filename, 'r') as file:
            return [line.strip().lower() for line in file.readlines()]
    except FileNotFoundError:
        logging.error(f"Plik {filename} nie został znaleziony. Używam domyślnych aplikacji.")
        return ['chrome', 'firefox', 'explorer', 'word', 'excel', 'powerpoint']

MONITORED_APPS = load_monitored_apps()

# Funkcja do monitorowania procesów
def monitor_processes(duration):
    start_time = time.time()
    end_time = start_time + duration
    app_usage = defaultdict(lambda: {'name': '', 'total_time': 0, 'start_times': []})

    while time.time() < end_time:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for proc in psutil.process_iter(['pid', 'name', 'create_time']):
            try:
                proc_name = proc.info['name'].lower()
                if any(app in proc_name for app in MONITORED_APPS):
                    pid = proc.info['pid']
                    app_usage[proc_name]['name'] = proc.info['name']
                    if len(app_usage[proc_name]['start_times']) == 0 or \
                            app_usage[proc_name]['start_times'][-1] != current_time:
                        app_usage[proc_name]['start_times'].append(current_time)
                    app_usage[proc_name]['total_time'] += 5  # Dodajemy 5 sekund użycia aplikacji
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        time.sleep(5)

    return app_usage

# Zapisanie wyników do pliku CSV
def save_to_csv(data, filename="app_usage_log.csv"):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Application', 'Total Time (seconds)', 'Start Times'])
            for app, info in data.items():
                writer.writerow([info['name'], info['total_time'], ', '.join(info['start_times'])])
    except Exception as e:
        logging.error(f"Błąd przy zapisywaniu do pliku CSV: {e}")

# Funkcja robienia zrzutu ekranu
def take_screenshot(filename="screenshot.png"):
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        print(f"Zrzut ekranu zapisany: {filename}")
    except Exception as e:
        logging.error(f"Błąd podczas robienia zrzutu ekranu: {e}")

# Funkcja wysyłająca logi na e-mail (wraz z plikami ze zrzutami ekranu)
def send_email(subject, body, to_email, from_email, from_password, files=[]):
    try:
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Treść wiadomości
        msg.attach(MIMEText(body, 'plain'))

        # Dodawanie załączników
        for file in files:
            with open(file, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={file}')
                msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print(f"E-mail wysłany do {to_email}")
    except smtplib.SMTPAuthenticationError:
        logging.error("Błąd uwierzytelniania SMTP. Sprawdź dane logowania.")
    except Exception as e:
        logging.error(f"Błąd przy wysyłaniu e-maila: {e}")

# Tworzenie raportu
def print_summary(data):
    print("\nSummary of Application Usage:\n")
    for app, info in data.items():
        total_seconds = info['total_time']
        hours, rem = divmod(total_seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"Application: {info['name']}")
        print(f"Total Usage: {int(hours)}h {int(minutes)}m {int(seconds)}s")
        print(f"Start Times: {info['start_times']}\n")

# Wykres aktywności aplikacji
def plot_usage(data):
    apps = [info['name'] for app, info in data.items()]
    usage_times = [info['total_time'] / 60 for app, info in data.items()]  # Czas w minutach

    plt.figure(figsize=(10, 6))
    plt.barh(apps, usage_times, color='skyblue')
    plt.xlabel('Usage Time (minutes)')
    plt.ylabel('Applications')
    plt.title('Application Usage Time')
    plt.tight_layout()
    plt.show()

# Powiadomienie o nadmiernym użyciu
def check_usage_alerts(data, alert_threshold):
    for app, info in data.items():
        if info['total_time'] > alert_threshold:
            print(f"Alert! {info['name']} has been used for more than {alert_threshold / 3600} hours!")

# Uruchomienie monitoringu i wysyłanie logów cyklicznie wraz z robieniem zrzutów ekranu
def monitor_and_send_logs():
    screenshot_timer = 0  # Zmienna, która będzie kontrolować czas robienia zrzutów ekranu
    while True:
        process_log = monitor_processes(duration_seconds)
        save_to_csv(process_log)
        print_summary(process_log)
        plot_usage(process_log)
        check_usage_alerts(process_log, alert_threshold)

        # Robienie zrzutu ekranu co określony interwał (np. co minutę)
        if screenshot_timer % screenshot_interval == 0:
            screenshot_file = f"screenshot_{int(time.time())}.png"
            take_screenshot(screenshot_file)

            # Wysyłanie e-maila z logami i zrzutem ekranu
            send_email(
                subject="Logi monitoringu aplikacji i zrzuty ekranu",
                body="Załączam logi z monitorowania aplikacji oraz zrzut ekranu.",
                to_email=email_settings.get('to_email', ''),
                from_email=from_email,
                from_password=from_password,
                files=["app_usage_log.csv", screenshot_file]
            )

        # Przerwa przed kolejnym cyklem monitorowania (np. 1 godzina)
        time.sleep(60)  # Każda pętla trwa 1 minutę
        screenshot_timer += 60  # Zwiększamy czas o 1 minutę

# Uruchomienie monitoringu i wysyłanie logów oraz zrzutów ekranu
monitor_and_send_logs()
