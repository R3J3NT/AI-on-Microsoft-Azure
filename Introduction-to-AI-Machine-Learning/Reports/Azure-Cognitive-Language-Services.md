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