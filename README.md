Opis funkcji:

    Biblioteki:
        psutil: Służy do monitorowania uruchomionych procesów (czyli aplikacji działających na komputerze).
        time: Używane do opóźnień w pętli monitorującej procesy i do pomiaru czasu.
        csv: Służy do zapisywania danych o aktywności aplikacji w pliku CSV.
        smtplib: Służy do wysyłania wiadomości e-mail za pomocą serwera SMTP.
        email.mime (MIMEMultipart, MIMEText, MIMEBase): Używane do tworzenia e-maili z załącznikami.
        matplotlib.pyplot: Używane do generowania wykresów z czasem spędzonym w aplikacjach.
        collections.defaultdict: Używane do przechowywania danych o uruchomionych aplikacjach.
        pynput.keyboard: Służy do rejestrowania naciśnięć klawiszy (keylogger).

Funkcje skryptu:
1. on_press(key):

    Opis: Funkcja ta jest wywoływana za każdym razem, gdy zostanie naciśnięty klawisz na klawiaturze.
    Działanie: Rejestruje naciśnięty klawisz i zapisuje go do globalnej listy key_logs.

2. start_keylogger():

    Opis: Inicjuje proces nasłuchiwania klawiatury w tle, który rejestruje naciśnięcia klawiszy za pomocą funkcji on_press.
    Działanie: Tworzy nowy wątek nasłuchiwania klawiatury, który nie koliduje z głównym działaniem skryptu.

3. monitor_processes(duration):

    Opis: Monitoruje aktywne procesy (uruchomione aplikacje) przez określony czas.
    Działanie: Przez zadany czas (w sekundach) monitoruje, które aplikacje są uruchomione. Zapisuje informacje o czasie trwania każdej aplikacji oraz kiedy dana aplikacja została uruchomiona.
    Dane wyjściowe: Zwraca słownik z nazwami aplikacji i czasem ich uruchomienia oraz łącznym czasem użycia.

4. save_to_csv(data, filename):

    Opis: Zapisuje dane o aktywności aplikacji do pliku CSV.
    Działanie: Tworzy plik CSV, w którym zapisuje się lista aplikacji, czas ich uruchomienia oraz łączny czas działania w sekundach.

5. save_key_logs(filename):

    Opis: Zapisuje naciśnięcia klawiszy (keylogi) do pliku tekstowego.
    Działanie: Tworzy plik tekstowy i zapisuje w nim każde naciśnięcie klawisza zapisane w globalnej liście key_logs.

6. send_email(subject, body, to_email, from_email, from_password, files):

    Opis: Wysyła wiadomość e-mail z załącznikami.
    Działanie: Tworzy wiadomość e-mail za pomocą MIMEMultipart, dodaje załączniki (pliki CSV z logami oraz keylogi), łączy się z serwerem SMTP (np. Gmail) i wysyła wiadomość.
    Argumenty:
        subject: Temat wiadomości e-mail.
        body: Treść wiadomości.
        to_email: Adres odbiorcy.
        from_email: Twój adres e-mail (nadawca).
        from_password: Hasło do twojego konta e-mail (może wymagać specjalnego hasła aplikacji w Gmailu).
        files: Lista plików, które mają być załączone do e-maila.

7. print_summary(data):

    Opis: Wyświetla podsumowanie aktywności aplikacji w terminalu.
    Działanie: Wyświetla listę monitorowanych aplikacji, czas ich uruchomienia oraz łączny czas działania w godzinach, minutach i sekundach.

8. plot_usage(data):

    Opis: Generuje wykres słupkowy przedstawiający czas spędzony w każdej aplikacji.
    Działanie: Tworzy wykres za pomocą matplotlib, który przedstawia czas (w minutach) spędzony w każdej z monitorowanych aplikacji.

9. check_usage_alerts(data, alert_threshold):

    Opis: Sprawdza, czy czas użycia aplikacji przekracza określony próg, i generuje ostrzeżenie w terminalu.
    Działanie: Sprawdza, czy dana aplikacja była używana dłużej niż określony czas (np. 30 minut). Jeśli tak, wyświetla ostrzeżenie w terminalu.

Główna część programu:
1. Uruchomienie keyloggera:

    Skrypt rozpoczyna nasłuchiwanie klawiatury w tle za pomocą funkcji start_keylogger().

2. Monitorowanie procesów:

    Skrypt monitoruje procesy przez określony czas (w przykładzie jest to 1 godzina). Używając funkcji monitor_processes(), zbiera dane o aktywnych aplikacjach i ich czasie działania.

3. Zapisywanie danych:

    Logi aktywności aplikacji są zapisywane w pliku CSV za pomocą funkcji save_to_csv().
    Logi z naciśnięciami klawiszy są zapisywane do pliku tekstowego za pomocą funkcji save_key_logs().

4. Wyświetlenie podsumowania i wykres:

    Funkcja print_summary() wyświetla podsumowanie aktywności aplikacji w terminalu.
    Funkcja plot_usage() generuje wykres z czasem spędzonym w każdej aplikacji.

5. Sprawdzenie ostrzeżeń:

    Funkcja check_usage_alerts() sprawdza, czy czas użycia aplikacji przekroczył określony próg, i wyświetla odpowiednie ostrzeżenie.

6. Wysyłanie e-maila:

    Na końcu skrypt wysyła wiadomość e-mail z załącznikami, które zawierają pliki CSV z logami aktywności aplikacji oraz plik z naciśnięciami klawiszy.

Jak działa cały skrypt:

    Uruchomienie keyloggera, który działa w tle i rejestruje naciśnięcia klawiszy.
    Monitorowanie uruchomionych aplikacji przez określony czas.
    Zapisanie logów do plików tekstowych i CSV.
    Wyświetlenie wyników monitorowania w terminalu oraz wygenerowanie wykresu.
    Wysyłanie logów na e-mail wraz z załącznikami.
    Sprawdzanie, czy czas użycia aplikacji przekracza ustalone limity i wyświetlanie ostrzeżeń.

Ważne informacje:

    Aby wysyłać e-maile, musisz skonfigurować odpowiednie ustawienia w Gmailu (np. hasło aplikacji lub włączyć dostęp dla mniej bezpiecznych aplikacji).
    Skrypt można łatwo dostosować do monitorowania innych aplikacji, zmieniając listę MONITORED_APPS.
    Skrypt działa na komputerze z systemem Windows, Linux lub macOS, ale dostęp do niektórych aplikacji może wymagać dodatkowych uprawnień administracyjnych.
