## Computer Vision API

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Computer Vision API, jest to serwis umożliwiający analizę zawartości filmów oraz zdjęć. W czasie rzeczywistym możemy otrzymać potrzebne informacje na temat tekstu, osób, przedmiotów a także innych elementów na temat przesłanych przez nas materiałów.

   2. **Opis działania serwisu**

      Serwis posiada wiele różnych endpointów oraz konfiguracji, które możemy wykorzystać w zależności od potrzeb. Schemat działania opiera się jednak na takim samym założeniu. Przesyłamy materiał do serwisu (mogą to być zarówno zdjęcia jak i filmy) za pomocą API a  w informacji zwrotnej otrzymujemy komplet interesujących nas informacji. Na przykład Face API pozwala nam na rozpoznać osoby na zdjęciu, wskazać miejsce występowania twarzy czy porównać twarz z innymi zdjęciami.

2. **Przypadki użycia serwisu**

   - Automatyczne rozpoznawanie osób na zdjęciu i klasyfikowanie ich pod względem występowania konkretnej osoby.
   - Digitalizacja dokumentów, rozpoznawanie tekstu ze zdjęć dokumentów i zapisywanie ich w formie cyfrowej.
   - Wykrywanie elementów z monitoringu, możemy na przykład automatycznie rozpoznać uszkodzenie / zniknięcie urządzenia.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Działanie serwisu opiera się na podobnych założeniach jak reszta Cognitive Services. Musimy zacząć od stworzenia odpowiedniego zasobu tak aby otrzymać prywatny klucz API oraz endpoint. Po otrzymaniu tych danych możemy rozpocząć wysyłanie zapytań do API z poziomu naszej aplikacji.

   2. **Koszty użytkowania serwisu**

      Dla regionu West Europe darmowa instancja pozwala nam wysłać 20 zapytań na minutę i do 5000 darmowych transakcji w miesiącu. Pakiet standard w zależności od typu zapytania kosztuje do 2,5$ za 1000 transakcji.

      

      