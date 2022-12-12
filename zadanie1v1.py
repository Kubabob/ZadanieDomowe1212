

def liczenie_znakow(tekst_wejsciowy):
    lista_znakow = {}
    suma_znakow = 0
    for wyraz in tekst_wejsciowy:
        for znak in wyraz:
            if znak == "," or znak == "." or znak == " " or znak == "\n" or znak == ";":
                pass
            elif znak not in lista_znakow:
                lista_znakow[str(znak)] = 1
                suma_znakow += 1
            else:
                lista_znakow[str(znak)] += 1
                suma_znakow += 1
    return sorted(lista_znakow.items()), suma_znakow


with open("plik1.txt", mode='r', encoding='utf-8') as plik_wejsciowy1:
    policzone_znaki = liczenie_znakow(plik_wejsciowy1)
    litery = policzone_znaki[0]
    suma_liter = policzone_znaki[1]


with open("plik_wyjsciowy1v1.txt", mode='w', encoding='utf-8') as plik_wyjsciowy1v1:
    for litera in litery:
        plik_wyjsciowy1v1.write(f'{litera[0]} {round((int(litera[1])/suma_liter)*100, 2)}%\n')





