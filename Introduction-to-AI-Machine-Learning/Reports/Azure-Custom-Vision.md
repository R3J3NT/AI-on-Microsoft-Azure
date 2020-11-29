## Custom Vision

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Custom Vision Servis jest jednym z najnowszych elementów usług Cognitive Service. Pozwala ona wytrenować w prosty sposób własny model, który będzie rozpoznawał wybrane przez nas grupy obrazów.

   2. **Opis działania serwisu**

      Serwis posiada pre-trenowane modele, które możemy douczyć na własnych danych tak aby w szybki sposób stworzyć rozpoznawanie potrzebnych nam obrazów. Dzięki oddzielnemu portalowi jesteśmy w stanie przeprowadzić cały proces w intuicyjny sposób, w interfejsie graficznym. Tak przygotowany model możemy wykorzystać w naszej aplikacji do rozpoznawania konkretnych typów obrazów.

2. **Przypadki użycia serwisu**

   - Przygotowanie aplikacji do rozpoznawania członków rodziny na zdjęciach i katalogowania ich w odpowiednich folderach.
   - Przetrenowanie modelu tak aby pozwalał rozpoznać części samochodowe, dzięki temu osoba nie znająca się na motoryzacji może zrobić zdjęcie elementu i dowiedzieć się co musi kupić  w sklepie.
   - Rozpoznawanie czy osoba ma założoną maseczkę na podstawie jej zdjęcia i na podstawie wyniku otwieranie drzwi w placówce.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Na początku musimy stworzyć nowy projekt w portalu Custom Vision Service. Podczas tworzenia możemy wybrać jedną z wielu pre-trenowanych domen na przykład: jedzenie. Następnie możemy dodać własny zbiór zdjęć oraz oznaczyć ich tagi i wyszkolić model. Po zakończeniu całego procesu możemy przetestować model i rozpocząć wykorzystywanie serwisu w naszej aplikacji.

   2. **Koszty użytkowania serwisu**

      Dla regionu West Europe, darmowy pakiet pozwala nam na wykonywanie 2 transakcji na sekundę. W obrębie tego pakietu możemy wgrać 5000 zdjęć i przeprowadzić 10000 analiz w ciągu miesiąca. Dla pakietu standard ilość transakcji podnosi się do 10 na sekundę a my płacimy 2$ za każde wgrane i przenalizowane 1000 zdjęć, 20$ za godzinę trenowania modelu oraz 0,70$ za przetrzymywanie 1000 zdjęć.

      

      