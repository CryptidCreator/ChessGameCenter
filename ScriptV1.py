import time
import datetime


class Player:

    def __init__(self, family_name, firstname, date_of_birth, gender, ranking):
        self.family_name = family_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking


class tournament:

    def __init__(self, name, place, date, tour, participants, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds_number = 0
        self.tour = tour
        self.participants = participants
        self.time_control = time_control
        self.description = description


# Tour en objet avec match en attribut


def set_player():
    print("Joueur")
    family_name = input("Nom de famille :")
    firstname = input("Prénom :")
    while True:
        try:
            date_of_birth = datetime.datetime.strptime(input("Date de naissance (Jour Mois Année) :"), '%d %m %Y')
        except ValueError:
            print("Vous devez rentrer une date valide. Ex : 14 07 1789")
        break
    while True:
        ask_gender = input("gender (M ou F) :")
        if ask_gender == "M" or ask_gender == "F":
            gender = ask_gender
            break
    ranking = 0
    player_Add = Player(family_name, firstname, date_of_birth, gender, ranking)
    return player_Add


def set_tournament():
    participants = []
    name = input("Nom:")
    place = input("Lieu :")
    while True:
        try:
            date = datetime.datetime.strptime(input("Date (Jour Mois Année) :"), '%d %m %Y')
        except ValueError:
            print("Vous devez rentrer une date valide. Ex : 14 07 1789")
        break
    tour = 0
    display_players(players)
    ask_indices = input("Joueur participant (Format : 1,2,3 ; Max. 8) :")
    indices = [int(n) for n in ask_indices.split(sep=",") if n.isdigit()]
    print(indices)
    for i in range(len(indices)):
        if 1 <= indices[i]:
            participants.append(players[indices[i] - 1])
    display_players(participants)
    print("Controle du temps (Bullet = 1; Blitz = 2; Coup Rapide = 3) :")
    ask_mode = input("Choississez un des trois modes :")    # While pour conditions
    if ask_mode == 1:
        time_control = "Bullet"
    elif ask_mode == 2:
        time_control = "Blitz"
    elif ask_mode == 3:
        time_control = "Coup rapide"
    else:
        print("Choississez 1, 2 ou 3")
#    description = input("Description :")
    tournament_Add = tournament(name, place, date, tour, participants, time_control, "Tkt bg")
    return tournament_Add


def display_player(var):
    print("Nom de Famille :", var.family_name)
    print("Prenom :", var.firstname)
    print("Date de naissance :", var.date_of_birth)
    print("Sexe :", var.gender)
    print("Classement :", var.ranking)


def display_players(list):
    for i in range(len(list)):
        print("Joueur", i + 1, ":")
        display_player(list[i])


def display_tournament(contest):
    print("Nom :", contest.name)
    print("Lieu :", contest.place)
    print("Date :", contest.date)
    print("Nombre de tours :", contest.rounds_number)
    print("Tournees :", contest.tour)
    print("Participants :")
    display_players(contest.participants)
    print("Contrôle du temps :", contest.time_control)
    print("Description : ", contest.description)

# modélisation match


player1 = Player("Feugueur", "Malik", "2000-03-13", "M", 0)
player2 = Player("Bulard", "Julien", "1992-05-27", "M", 1)
player3 = Player("Maukeur", "Feli", "1999-09-09", "F", 2)
players = [player1, player2, player3]
while True:
    print("MENU :")
    print("- CREER LES JOUEURS : 1")
    print("- AFFICHER LES JOUEURS : 2")
    print("- CREER LE TOURNOI : 3")
    print("- AFFICHER LE TOURNOI : 4")
    print("- QUITTER L'APPLICATION : 0")
    Chiffre = int(input("CHOIX :"))
    if Chiffre == 1:
        players.append(set_player())
    elif Chiffre == 2:
        print("")
        display_players(players)
        print("")
    elif Chiffre == 3:
        tournament = set_tournament()
    elif Chiffre == 4:
        print("")
        display_tournament(tournament)
        print("")
    elif Chiffre == 0:
        break
    else:
        print("")
        print("Veuillez choisir un chiffre disponible!")
        print("")

# Git init puis git remote add

# Aprés lancement du tournoi :
# Generer les matchs et ajouter round (Objets)
# Faire tour et match pour un round. Afficher match et demander les résultat
# Boucle
# Donner les resultats
# calculer le classement
# Donner les prochains matchs
# Fin de boucle après la finale
# Donner le classement

# enregistrement (à faire quand tous est fonctionnel)
