Opis działania skryptu:

Skrypt ma na celu monitorowanie aktywności aplikacji na komputerze, rejestrowanie naciśnięć klawiszy oraz wysyłanie wynikowych logów na adres e-mail. Może być stosowany np. do kontrolowania aktywności dzieci na komputerze, pozwalając na zbieranie danych o tym, jakie programy były używane oraz jakie klawisze były naciskane.
Funkcje skryptu:

    Monitorowanie uruchomionych aplikacji:
        Skrypt regularnie sprawdza, które aplikacje są uruchomione na komputerze.
        Rejestruje czas, w którym aplikacje zostały uruchomione, oraz łączny czas ich aktywności.
        Monitorowane są wybrane aplikacje (można zdefiniować, jakie programy mają być śledzone, np. przeglądarki internetowe, programy do edycji dokumentów itp.).

    Rejestracja naciśnięć klawiszy (keylogger):
        Skrypt rejestruje wszystkie naciśnięcia klawiszy na klawiaturze.
        Każde naciśnięcie jest zapisywane w pliku tekstowym.
        Keylogger działa w tle, nie zakłócając pracy innych funkcji skryptu.

    Generowanie raportu z aktywności aplikacji:
        Po zakończeniu monitorowania, skrypt generuje raport zawierający listę aplikacji, które były uruchomione, oraz czas ich aktywności.
        Raport ten jest zapisywany w pliku CSV (plik tekstowy z danymi oddzielonymi przecinkami), który można otworzyć w Excelu lub innych arkuszach kalkulacyjnych.

    Generowanie wykresu aktywności aplikacji:
        Skrypt tworzy wykres przedstawiający czas spędzony w poszczególnych aplikacjach.
        Wykres ten wizualizuje, ile minut było spędzonych w każdej aplikacji, co ułatwia analizę.

    Powiadomienia o nadmiernym użyciu aplikacji:
        Skrypt sprawdza, czy dana aplikacja była używana przez dłuższy czas niż określony próg (np. 30 minut).
        Jeśli czas ten zostanie przekroczony, skrypt wyświetla ostrzeżenie w terminalu.

    Wysyłanie logów na e-mail:
        Po zakończeniu monitorowania, skrypt wysyła wiadomość e-mail z załączonymi plikami: logami naciśnięć klawiszy oraz raportem z aktywności aplikacji.
        Wiadomość e-mail może być wysyłana przez Gmaila lub inne serwery pocztowe, pod warunkiem odpowiedniej konfiguracji.
        W wiadomości znajduje się temat, treść oraz załączniki z danymi.

Użyte technologie:

    Python: Skrypt został napisany w języku Python i korzysta z kilku popularnych bibliotek, takich jak psutil (do monitorowania procesów), pynput (do rejestrowania naciśnięć klawiszy) oraz smtplib (do wysyłania e-maili).
    SMTP: Do wysyłania wiadomości e-mail używany jest protokół SMTP (Simple Mail Transfer Protocol), który jest standardem do przesyłania poczty internetowej. W przykładzie korzysta się z serwera Gmail.
    Matplotlib: Ta biblioteka służy do generowania wykresów, które przedstawiają czas spędzony w różnych aplikacjach.

Proces działania:

    Uruchomienie skryptu: Po uruchomieniu skrypt zaczyna nasłuchiwanie naciśnięć klawiszy oraz monitorowanie uruchomionych aplikacji.

    Monitorowanie aktywności: Skrypt regularnie sprawdza, które aplikacje są aktywne i jak długo były uruchomione. Rejestruje również każde naciśnięcie klawisza.

    Zapis logów: Pod koniec okresu monitorowania (który można ustawić) skrypt zapisuje wszystkie zebrane dane do plików: jeden plik CSV z raportem aplikacji oraz plik tekstowy z naciśnięciami klawiszy.

    Wizualizacja danych: Skrypt generuje wykres z czasem spędzonym w aplikacjach, co pomaga w szybkiej analizie danych.

    Wysyłanie e-maila: Po zakończeniu monitorowania skrypt automatycznie wysyła wiadomość e-mail na podany adres, z załączonymi plikami logów.

Praktyczne zastosowanie:

    Kontrola rodzicielska: Skrypt może być używany do monitorowania aktywności dzieci na komputerze, rejestrowania, jakie aplikacje są uruchamiane oraz jak długo były używane.
    Monitorowanie efektywności pracy: Może być również wykorzystany w biurze do monitorowania czasu spędzanego w poszczególnych programach przez pracowników (z ich wiedzą).
    Zarządzanie czasem: Użytkownicy mogą śledzić własne nawyki związane z korzystaniem z komputera, aby lepiej zarządzać czasem spędzanym w różnych aplikacjach.

Ważne kwestie:

    Prawa i prywatność: Wykorzystanie tego rodzaju narzędzi musi być zgodne z prawem i etyką. Monitorowanie aktywności użytkowników bez ich zgody może być nielegalne w wielu krajach, w tym w Norwegii.
    Bezpieczeństwo: Logi z naciśnięciami klawiszy oraz inne dane powinny być przechowywane i zabezpieczane w odpowiedni sposób, aby nie dostały się w niepowołane ręce.

Skrypt ten jest wszechstronnym narzędziem do monitorowania aktywności na komputerze i zarządzania czasem, które można dostosować do różnych zastosowań, takich jak kontrola rodzicielska lub analiza produktywności.
