import datetime


class Player:

    def __init__(self, family_name, firstname, date_of_birth, gender, points):
        self.family_name = family_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.points = points


class Tournament:

    def __init__(self, name, place, date, participants, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.round_number = 0   # Pas modifiable pendant la création
        self.rounds = []        # Pas modifiable pendant la création
        self.participants = participants
        self.time_control = time_control
        self.description = description


class Round:

    def __init__(self, matches):
        self.matches = matches


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
    points = 0
    player_Add = Player(family_name, firstname, date_of_birth, gender, points)
    return player_Add


def set_tournament():
    participants = []
    name_set = input("Nom:")
    place_set = input("Lieu :")
    while True:
        try:
            date_set = datetime.datetime.strptime(input("Date (Jour Mois Année) :"), '%d %m %Y')
        except ValueError:
            print("Vous devez rentrer une date valide. Ex : 14 07 1789")
        break
    display_players(players)
    ask_indices = input("Joueur participant (Format : 1,2,3,4 [nbre pair] ; Max. 8) :")
    indices = [int(n) for n in ask_indices.split(sep=",") if n.isdigit()]
    print(indices)
    for i in range(len(indices)):
        if 1 <= indices[i]:
            participants.append(players[indices[i] - 1])
    display_players(participants)
    print("Controle du temps (Bullet = 1; Blitz = 2; Coup Rapide = 3) :")
    while True:
        ask_mode = int(input("Choississez un des trois modes :"))
        if ask_mode == 1:
            time_control_set = "Bullet"
            break
        elif ask_mode == 2:
            time_control_set = "Blitz"
            break
        elif ask_mode == 3:
            time_control_set = "Coup rapide"
            break
        else:
            print("Choississez 1, 2 ou 3")
#    description = input("Description :")
    tournament_Add = Tournament(name_set, place_set, date_set, participants, time_control_set, "Tkt bg")
    return tournament_Add


def display_player(var):
    print("Nom de Famille :", var.family_name)
    print("Prenom :", var.firstname)
    print("Date de naissance :", var.date_of_birth)
    print("Sexe :", var.gender)
    print("Points :", var.points)


def display_players(list):
    for i in range(len(list)):
        print("Joueur", i + 1, ":")
        display_player(list[i])


def display_tournament(contest):
    print("Nom :", contest.name)
    print("Lieu :", contest.place)
    print("Date :", contest.date)
    print("Nombre de tours :", contest.round_number)
    print("Tournees :", contest.rounds)
    print("Participants :")
    display_players(contest.participants)
    print("Contrôle du temps :", contest.time_control)
    print("Description : ", contest.description)


def display_match(tupl):
    print("Match :")
    for i in range(len(tupl)):
        temp = tupl[i]
        print("Joueur : ")
        print(temp.family_name, temp.firstname)


def ask_result(tupl):
    while True:
        print("Premier joueur gagnant : 1")
        print("Deuxième joueur gagnant : 2")
        print("Égalité : 3")
        ask_r = int(input("Quel est le résultat du match? :"))
        if ask_r == 1:
            temp = tupl[0]
            temp.points += 1
            break
        elif ask_r == 2:
            temp = tupl[1]
            temp.points += 1
            break
        elif ask_r == 3:
            for i in range(2):
                temp = tupl[i]
                temp.points += 1/2
            break
        else:
            print("Choississez 1, 2 ou 3")


def points_update(var):
    sorted_list = [""] * len(var)
    for j in range(len(var)):
        for i in range(len(var)):
            short = 0
            temp_i = var[i]
            if short < temp_i.points:   # AttributeError: 'int' object has no attribute 'points'
                short = temp_i.points
                sorted_list[j] = var[i]
                var[i] = 0
    var = sorted_list
    return var


def play_round(competition):
    playing_matches = []
    done_matches = []
    points_update(competition.participants)
    half = int(len(competition.participants)/2)
    for j in range(half):
        duo = (competition.participants[j], competition.participants[j + int(half)])
        playing_matches.append(duo)
        display_match(duo)
    for duo in playing_matches:
        result = ask_result(duo)
        match = duo, result
        done_matches.append(match)


player1 = Player("Feugueur", "Malik", "2000-03-13", "M", 0)
player2 = Player("Bulard", "Julien", "1992-05-27", "M", 0)
player3 = Player("Maukeur", "Feli", "1999-09-09", "F", 0)
player4 = Player("Juste", "Innome", "1990-11-06", "M", 0)
players = [player1, player2, player3, player4]

tournament = Tournament("CG-Senlis", "Senlis", "2021-06-02", players, "Bullet", "Tkt bg")

while True:
    print("MENU :")
    print("- CREER LES JOUEURS : 1")
    print("- AFFICHER LES JOUEURS : 2")
    print("- CREER LE TOURNOI : 3")
    print("- AFFICHER LE TOURNOI : 4")
    print("- LANCER LE TOURNOI : 5")
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
    elif Chiffre == 5:
        play_round(tournament)
    elif Chiffre == 0:
        break
    else:
        print("")
        print("Veuillez choisir un chiffre disponible!")
        print("")


# Aprés lancement du tournoi :
# Faire round et match pour un round. Afficher match et demander les résultat
# Boucle
# Donner les resultats
# calculer le classement
# Donner les prochains matchs
# Fin de boucle après la finale
# Donner le classement

# enregistrement (à faire quand tous est fonctionnel)
