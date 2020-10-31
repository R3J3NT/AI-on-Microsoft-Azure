# Azure Cognitive Language Services



# Azure Content Moderator

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Azure Content Moderator wspomaga użytkowników w moderowaniu treści takich jak zdjęcia, tekst a nawet filmy. Pozwala wychwycić i odpowiednio zaregować na nieodpowiednie treści zawarte w wybranych materiałach.

   2. **Opis działania serwisu**

      Serwis pozwala analizować dane zebrane z wielu źródeł, na przykład takich jak, fora dyskusyjne, boty, dokumenty czy strony internetowe. Analiza odbywa się poprzez wysłanie zapytania z danymi do odpowiedniego API. Jako odpowiedź otrzymujemy listę niepożądanych słów, informację do jakiego typu należą a także dodatkowe informacje na temat występujących danych osobowych. Na podstawie danych zwrotnych możemy zdecydować czy dany plik jest poprawny, czy może musimy podjąć jakąś akcję z nim związaną - na przykład przesłać go do akceptacji zanim zostanie opublikowany.

2. **Przypadki użycia serwisu**

   - Moderowanie komentarzy na blogu - w przypadku wykrycia nieodpowiednich słów, przed automatyczną publikacją komentarza możemy go przesłać do akceptacji.
   - Podczas publikowania treści do sieci możemy zweryfikować czy użytkownik nie dodaje plików z danymi personalnymi. W przypadku wykrycia takiej sytuacji możemy zablokować dodawanie wybranego elementu tak, żeby nie doszło do wycieku danych personalnych.
   - Wychwytywanie obraźliwych wiadomości w czasie rzeyczwistym - na przykład podczas transmisji na żywo, w przypadku wykrycia daną wiadomość możemy natychmiast usunąć.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Przed rozpoczęciem korzystania z analizy materiałów musimy założyć odpowiednie zasoby. Po odpowiedniej konfiguracji, ustawieniu unikalnej nazwy zasobu a także wybraniu odpowiedniej subskrypcji otrzymujemy swój prywatny subscription key - który możemy wykorzystać do wysyłania zapytań.

   2. **Koszty użytkowania serwisu**

      Koszty serwisu zależą oczywiście od wybranego regionu, w przypadku West Europe możemy użytkować darmowy pakiet (ograniczeniem jest maksymalnie jedno zapytanie na sekundę oraz maksymalnie 5000 transakcji w miesiącu). W przypadku pakietu standard możemy wysyłać zapytania z częstotliwością 10 na sekundę a 1000 zapytań kosztuje nas 1$ - w przypadku gdy wykonamy mniej niż 1M transakcji.





# Language Understanding Intelligent Service (LUIS)

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      LUIS pozwala na inteligentną interakcję z użytkownikiem aplikacji. Z wykorzystaniem machine leariningu serwis ten pozwala nam przewidzieć ogólne znaczenie tekstu przesłanego przez użytkownika a także wyciągnać z niego konkretne, interesujące nas dane.

   2. **Opis działania serwisu**

      Serwis pozwala nam na zrozumienie intencji użytkownika na podstawie dostarczonej wypowiedzi. Dodatkowo jako odpowiedź otrzymujemy także słowa lub frazy, które są kluczowe w danym sformuowaniu (miejsce, przedmiot, data czy imię). Takie działanie pozwala nam na analizę wiadomości dostarczonych przez użytkownika i podjęcie odpowiedniego działania bez konieczności reakcji ze strony człowieka.

2. **Przypadki użycia serwisu**

   - Bot służący do rezerwacji biletów lotniczych, na podstawie zapytania użytkownika jesteśmy w stanie odczytać skąd, dokąd i dla ilu osób użytkownik chce nabić bilet.
   - Inteligentny formularz składania zamówienia na jedzenie, nie trzeba mozolnie wypełniać kategorii i wielu dodatkowych parametrów a wystarczy wpisać na przykład: Dwie pizze na grubym cieście z szynką i ananasem.
   - Umawianie się na wizytę do lekarza za pomocą czatu. Na podstawie specjalizacji, i terminu bot jest w stanie zaproponować konkretnego lekarza i placówkę.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Po utworzeniu odpowiedniego zasobu i jego konfiguracji mamy dostęp do narzędzia pozwalającego nam douczanie modelu do naszych potrzeb. Możemy wprowadzać odpowiednie intencje a także korygować nieodpowiednio sklasyfikowane zapytania. Po opublikowaniu naszego modelu możemy wysyłać do niego zapytania API z dowolnej aplikacji.

   2. **Koszty użytkowania serwisu**

      Darmowy pakiet dla regionu West Europe pozwala nam wykonać 5 zapytań na sekundę i maksymalnie do 10 tysięcy transakcji miesięcznie. W przypadku pakietu standardowego częstotliwośc możę wynosić 50 zapytań na sekundę a za 1000 transakcji płacimy 1,5$ mesięcznie.

      

      

      

# Text Analytics API

1. **Wstęp**

   1. **Wstępne przedstawienie serwisu**

      Test Analytics pozwala na analizę dostarczonego do serwisu tekstu. Jako efekt jego działania możemy otrzymać informację na temat nastawienia twócy, języka w jakim tekst jest napisany a także wydobyć z niego kluczowe frazy.

   2. **Opis działania serwisu**

      Serwis pozwala nam na lepsze zrozumienie intencji osoby który napisała dany tekst. Mogą to być opinie w internecie, komentarze czy wiadomości dostarczone do firmy. Serwis pozwala nam wydobyć inormacje z dostarczonego tekstu, klasyfikacja nacehcowania tekstu odbywa się w skali od 0 do 1. Im bliżej do wartości 1 oznacza to, że tekst jest bardziej pozytywny, im bliżej do 0 to tekst jest nacechowany bardziej negatywnie.

2. **Przypadki użycia serwisu**

   - Analiza komentarzy w sieci dotyczących naszej firmy, jeżeli znajdzemy opinie nacechowane bardzo negatywnie, możemy zareagować z odpowiednią odpowiedzią na dany komentarz.
   - Filtr przed wpuszczeniem wiadomości do komunikatora, jeżeli nie chcemy negatywnych treści w naszej społecznośći możemy odrzucić wiadomości, które zostaną sklasyfikowane jako nacechowane negatywnie.
   - Jeżeli nasza firma obsługuje klientów z róznych krajów, możemy wykryć język wiadomości przesłanej do supportu i przypisać jej do odpowiedniego konsultanta, który zna dany język.

3. **Jak pracować z serwisem**

   1. **Opis użycia serwisu**

      Aby korzystać z serwisu musimy stworzyć odpowiedni zasób i uzyskać dostęp do klucza dostępowego. Następnie możemy wysyłać zapytania API z tekstem do analizy z dowolnego miejsca.

   2. **Koszty użytkowania serwisu**

      W przypadku Text Analytics i regionu West Europe, mamy bardzo dużo dostępnych pakietów. Pakiet darmowy umożliwia nam wysłanie maksymalnie 5000 zapytań miesięcznie. Pakiet standard oferuje nam 1000 zapytań za 2$ jeżeli wykonamy mniej niż 500 tysięcy zapytań w miesiącu.

      

      

      





