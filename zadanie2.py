def znajdowanie_liczb(tekst_wejsciowy):
    lista_liczb = []
    for linia in tekst_wejsciowy:
        for wyraz in linia.split():
            try:
                lista_liczb.append(float(wyraz))
            except ValueError:
                pass

    return lista_liczb

with open("plik2.txt", mode='r', encoding='utf-8') as plik_wejsciowy2:
    liczby = znajdowanie_liczb(plik_wejsciowy2)

with open("plik_wyjsciowy2.txt", mode='w', encoding='utf-8') as plik_wyjsciowy2:
    for liczba in liczby:
        plik_wyjsciowy2.write(f'{liczba}\n')


