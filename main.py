import os
import string

FOLDER_GLOWNY = r"C:\Users\DTP01\Desktop\Zdjecia"

ROZSZERZENIA = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.tiff', '.psd'}

def przemianuj_plik():
    for folder in os.listdir(FOLDER_GLOWNY):
        sciezka_folderu = os.path.join(FOLDER_GLOWNY, folder)

        if not os.path.isdir(sciezka_folderu):
            continue
        pliki = os.listdir(sciezka_folderu)

        indeks = 0

        for plik in pliki:
            nazwa, rozszerzenie = os.path.splitext(plik)
            rozszerzenie = rozszerzenie.lower()

            if rozszerzenie not in ROZSZERZENIA:
                continue

            if nazwa.startswith(folder):
                print(f"Pomijam {plik} - już poprawnie nazwany")
                continue

            litera = string.ascii_lowercase[indeks]

            nowa_nazwa = folder + litera + rozszerzenie

            nowa_sciezka = os.path.join(sciezka_folderu, nowa_nazwa)

            while os.path.exists(nowa_sciezka):
                indeks += 1
                litera = string.ascii_lowercase[indeks]
                nowa_nazwa = folder + litera + rozszerzenie
                nowa_sciezka = os.path.join(sciezka_folderu, nowa_nazwa)

            stara_sciezka = os.path.join(sciezka_folderu, plik)

            os.rename(stara_sciezka, nowa_sciezka)

            print(f"{plik} -> {nowa_nazwa}")

            indeks += 1


przemianuj_plik()
print("Gotowe!")