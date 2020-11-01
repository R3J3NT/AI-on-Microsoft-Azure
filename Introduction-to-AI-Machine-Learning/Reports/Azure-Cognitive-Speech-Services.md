# Azure Cognitive Speech Services



## Speech-to-text

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Speech to text nazywany inaczej rozpoznawaniem mowy, pozwala nam w czasie rzeczywistym zapisać nagranie audio w formie tekstowej. Na podstawie takiej transkrypcji nasz system może podjąć kolejne działania, które nie były by możliwe bezpośrednio z nagrania dźwiękowego.

   2. **Opis działania serwisu**

      Serwis pozwala nam wykorzystać wejście audio jako podstawę do podejmowania kolejnych działań. Za pomocą speech to text otrzymujemy translacje nagrania audio na tekst, który możemy później wykorzystać. Tekstowy zapis nagrania możemy wykorzystać do podjęcia decyzji, na przykład jako wejście do QnA Maker.

      

2. **Przypadki użycia serwisu**

   - Translacja nagrania głosowego w restauracji tak aby można było złożyć zamówienie za pomocą łączności przez komunikator głosowy.
   - Tworzenie napisów do nagrania wideo w czasie rzeczywistym z tłumaczeniem na zadane języki.
   - Digitalizacja w postaci tekstu, historycznych nagrań audio zebranych w zbiorach biblioteki.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Po stworzeniu odpowiednich zasobów otrzymuje dostęp do klucza oraz endpointu, na podstawie któych możemy wysyłać pliki do translacji. Z wykorzystaniem tych dwóch wartości, możemy odpytywać serwis o translacje zadanego pliku audio do tekstu.

   2. **Koszty użytkowania serwisu**

      W przypadku pakietu darmowego możemy wykorzystać 5 godzin nagrań audio na miesiąc. W pakiecie standard płacimy 1$ za kazdą godzinę nagrania audio.

      

## Text-to-Speech

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Text to speech jest przeciwieństwem poprzedniego serwisu, pozwala nam on wygenerować nagranie audio z wysłanego tekstu. Proces ten nazywany jest syntezacją dźwięku i pozwala tworzyć głosowe komunikaty.

   2. **Opis działania serwisu**

      Serwis pozwala nam tworzyć reprodukcję ludziej mowy, z uwzględnieniem całej charakterystyki ludzkiego modelu głosu. Na podstawie dostarczonego tekstu serwis jest w stanie stworzyć nagranie dźwiękowe które odwzorowuje zapis tekstowy, tak jakby został on nagrany przez lektora.

2. **Przypadki użycia serwisu**

   - Generowanie informacji dźwiękowych na podstwie tekstu na stronie dla osób niewidomych.
   - Usprawnienie botów o komunikację dźwiękową, wygenerowaną odpowiedź tekstową możemy zamienić na komunikat audio.
   - Tworzenie asystentów głosowych, którzy jako informację zwrtoną lub zapytanie mogą używać mowy a nie tylko tekstu.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Po stworzeniu odpowiednich zasobów, otrzymujemy dostęp do klucza oraz endpointa na który możemy wysyłać zapytania. Podczas wysyłania zapytania możemy wybrać także typ głosu jaki ma zostać wybrany do generacji dźwięku.

   2. **Koszty użytkowania serwisu**

      W przypadku darmowego pakietu możemy przesłać 5 milionów znaków tekstu na miesiąc dla standardowego typu głosu. W pakiecie standardowym płacimy 4$ za 1 Milion znaków.



## Translate speech

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Translate speech pozwala nam na tłumaczenie mowy na inny język. Dzięki temu umożlwia on komunikację osób które posłgują się różnymi językami.

   2. **Opis działania serwisu**

      Cały proces opiera się na zamianie pliku audio na tekst, następnie tekst zostaje poddany translacji a na koniec może zostać wygenerowny plik audio w procesie syntezacji dźwięku. Dzięki takiemu zabiegowi dana wypowiedź może został przetłumaczona na inny język i odtworzona tak aby była zrozumiała dla drugiego rozmówcy.

2. **Przypadki użycia serwisu**

   - Translacja komunikatów systemowych do różnych języków.
   - System wspomagający porozumiewanie się osób w różnych językach.
   - System tłumaczący w czasie rzeczywistym wystąpienia publiczne do różnych języków.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Koniecznie jest stworzenie odpowiednich zasobów a także otrzymanie klucza i endpointu do którego wysyłać będziemy zapytania. Podczas tworzenia aplikacji musimy także skonfigurować z jakiego i do jakich języków powinny być tłumaczone nagrania.

   2. **Koszty użytkowania serwisu**

      W przypadku pakietu darmowego w regionie West Europe możemy wykorzystać 5 godzin nagrań audio w ciągu miesiąca. W przypadku planu standardowego płacimy 2,50 za godzine nagrania audio.

      

