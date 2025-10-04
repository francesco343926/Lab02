from csv import reader

def carica_da_file(file_path):
    try:
        daLeggere= open(file_path, "r", encoding="utf-8")
        numsezioni= int(daLeggere.readline())
        filecsv= reader(daLeggere)
        biblioteca=[]
        for riga in filecsv:
            diz= dict()
            diz["nomelibro"]= riga[0]
            diz["autore"]= riga[1]
            diz["anno"]= int(riga[2])
            diz["pagine"] = int(riga[3])
            diz["sezione"] = int(riga[4])
            biblioteca.append(diz)
        daLeggere.close()
        return biblioteca
    except FileNotFoundError:
        return None




def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
   diz= dict()
   diz["nomelibro"] = titolo
   diz["autore"] = autore
   diz["anno"] = anno
   diz["pagine"] = pagine
   diz["sezione"] = sezione
   biblioteca.append(diz)
   daScrivere = open(file_path, "a")
   for valore in diz.values():
       daScrivere.write(str(valore))
       daScrivere.write(",")
   daScrivere.close()



def cerca_libro(biblioteca, titolo):
    trovato = False
    for libro in biblioteca:
        if libro["nomelibro"].lower()== titolo.lower():
            trovato= True
            risultato= f"{libro["nomelibro"]},{libro["autore"]},{str(libro["anno"])},{str(libro["pagine"])},{str(libro["sezione"])}"
            return risultato
        if not trovato:
            return "libro non trovato"


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    titoliscelti =[]
    for libro in biblioteca:
        if libro["sezione"]== sezione:
            titoliscelti.append(libro["nomelibro"])
    if not titoliscelti:
        return None
    ordinati = sorted(titoliscelti)
    return ordinati





def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

