import random

def jeu_de_devinettes():
    print("Bienvenue au jeu de devinettes!")
    nombre_secret = random.randint(1, 100)
    tentatives = 0

    while True:
        devinette = input("Devinez le nombre entre 1 et 100: ")
        tentatives += 1

        try:
            devinette = int(devinette)
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if devinette < nombre_secret:
            print("Trop bas!")
        elif devinette > nombre_secret:
            print("Trop haut!")
        else:
            print(f"Bravo! Vous avez deviné le nombre en {tentatives} tentatives.")
            break

jeu_de_devinettes()
