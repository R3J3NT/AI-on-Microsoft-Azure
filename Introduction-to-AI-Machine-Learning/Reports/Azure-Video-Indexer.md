## Video Indexer

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Azure Video Indexer jest to serwis pozwalający na wydobycie ważnych dla nas informacji z plików multimedialnych. W zakres pracy wchodzi wykrywanie twarzy, rozpoznawanie tekstu, podział scen czy wydobycie elementów widocznych na filmie.

   2. **Opis działania serwisu**

      Do serwisu możemy wgrywać filmy wideo w formatach takich jak: WMV, MOV, MPG, and AVI. Pliki mogą być wgrywane za pomocą adresu URL a także za pośrednictwem zapytań do API. Po wgraniu filmu, możemy wyciągnąć z portalu informacje na jego temat. W skład informacji wchodzą między innymi: zidentyfikowane twarze, transkrypcja dźwięku, wykryty text na filmie czy emocje wykryte z mowy.

2. **Przypadki użycia serwisu**

   - Usprawnienie wyszukiwarki filmów o przeszukiwanie zawartości filmu, możemy odwołać się do konkretnej minuty filmu w której występuje dany element.
   - Stworzenie portalu, który automatycznie generuje napisy i tłumaczy je na inne języki na podstawie wgranych filmów.
   - Klasyfikacja filmów na podstawie emocji aktorów.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Aby rozpocząć korzystanie z serwisu musimy założyć subskrypcję na portalu Wideo Indexer. Dzięki temu możemy zdobyć klucz API, który będzie nam potrzebny do wysyłania zapytań.

   2. **Koszty użytkowania serwisu**

      Darmowy pakiet umożliwia 10 godzin indeksowania dla użytkowników strony oraz 40 godzin indeksowania dla użytkowników API. Jeżeli chcemy procesować większą ilość danych należy podłączyć swoją własną instancję Azure Media Services.

      