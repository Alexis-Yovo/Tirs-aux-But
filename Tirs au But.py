import random

def tir_au_but():
    return random.choice([True, False])  # True si le tir est marqué, False sinon

def seance_tirs_au_but(equipe1, equipe2, tentatives):
    score_equipe1 = 0  
    score_equipe2 = 0

    for i in range(tentatives):
        if tir_au_but():
            score_equipe1 += 1  
            print(f"Tir {i + 1} de {equipe1}: But !")
        else:
            print(f"Tir {i + 1} de {equipe1}: Raté !")

        if tir_au_but():
            score_equipe2 += 1  
            print(f"Tir {i + 1} de {equipe2}: But !")
        else:
            print(f"Tir {i + 1} de {equipe2}: Raté !")

        # Vérification des conditions de fin de séance  
        if (i == 2 and score_equipe1 == 3 and score_equipe2 == 0) or \
           (i == 2 and score_equipe1 == 0 and score_equipe2 == 3) or \
           (i == 3 and score_equipe1 == 4 and score_equipe2 == 2) or \
           (i == 3 and score_equipe1 == 2 and score_equipe2 == 4):
            print(f"\n{equipe1} - {equipe2} : Fin des tirs au but, {equipe1 if score_equipe1 > score_equipe2 else equipe2} remporte !")
            print(f"Score final : {equipe1} {score_equipe1} - {score_equipe2} {equipe2}")
            return

        # Vérification si une équipe est assurée de gagner  
        if score_equipe1 > score_equipe2 + (tentatives - (i + 1)):
            print(f"\n{equipe1} remporte la séance de tirs au but ! (Impossible de rattraper)")
            print(f"Score final : {equipe1} {score_equipe1} - {score_equipe2} {equipe2}")
            return  
        elif score_equipe2 > score_equipe1 + (tentatives - (i + 1)):
            print(f"\n{equipe2} remporte la séance de tirs au but ! (Impossible de rattraper)")
            print(f"Score final : {equipe1} {score_equipe1} - {score_equipe2} {equipe2}")
            return

    print(f"\nScore final : {equipe1} {score_equipe1} - {score_equipe2} {equipe2}")

    # Vérification de l'égalité  
    while score_equipe1 == score_equipe2:
        print("\nÉgalité, passage à la mort subite !")
        if tir_au_but():
            score_equipe1 += 1  
            print(f"{equipe1} marque !")
        else:
            print(f"{equipe1} rate !")

        if tir_au_but():
            score_equipe2 += 1  
            print(f"{equipe2} marque !")
        else:
            print(f"{equipe2} rate !")

        print(f"Score actuel : {equipe1} {score_equipe1} - {score_equipe2} {equipe2}")

    # Afficher le résultat final  
    if score_equipe1 > score_equipe2:
        print(f"\n{equipe1} remporte la séance de tirs au but !")
    else:
        print(f"\n{equipe2} remporte la séance de tirs au but !")

# Appel de la fonction pour simuler une séance de tirs au but  
seance_tirs_au_but("Espagne", "Angleterre", 5)
