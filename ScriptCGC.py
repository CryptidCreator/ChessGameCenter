import datetime
from tinydb import TinyDB


class Player:

    def __init__(self, family_name, firstname, date_of_birth, gender, points):
        self.family_name = family_name
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.points = points


class Tournament:

    def __init__(self, name, place, date, round_number, participants, time_control, description):
        self.name = name
        self.place = place
        self.date = date
        self.round_number = round_number
        self.participants = participants
        self.time_control = time_control
        self.description = description


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
    rounds_set = int(len(participants)/2)
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
    description = input("Description :")
    tournament_Add = Tournament(name_set, place_set, date_set, rounds_set, participants, time_control_set, description)
    return tournament_Add


def display_player(var):
    print("Nom de Famille :", var.family_name)
    print("Prenom :", var.firstname)
    print("Date de naissance :", var.date_of_birth)
    print("Sexe :", var.gender)
    print("Points :", var.points)


def display_players(tab):
    for i in range(len(tab)):
        print("Joueur", i + 1, ":")
        display_player(tab[i])


def display_tournament(contest):
    print("Nom :", contest.name)
    print("Lieu :", contest.place)
    print("Date :", contest.date)
    print("Nombre de tours :", contest.round_number)
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
    print("")


def ask_result(tupl, tab):
    while True:
        print("\n")
        for i in range(len(tupl)):
            temp = tupl[i]
            print(str(temp.family_name), str(temp.firstname), "gagnant :", str(i+1))
        print("Égalité : 3")
        ask_r = int(input("Quel est le résultat du match? :"))
        if ask_r == 1:
            temp = tupl[0]
            n = 0
            while temp != tab[n]:
                n += 1
            tab[n].points += 1
            return temp
        elif ask_r == 2:
            temp = tupl[1]
            n = 0
            while temp != tab[n]:
                n += 1
            tab[n].points += 1
            return temp
        elif ask_r == 3:
            for i in range(2):
                temp = tupl[i]
                n = 0
                while temp != tab[n]:
                    n += 1
                tab[n].points += 1/2
            return "Égalité"
        else:
            print("Choississez 1, 2 ou 3")


def points_update(participants):
    sorted_tab = sorted(participants, key=lambda Player: Player.points, reverse=True)
    return sorted_tab


def play_round(competition):
    play = len(competition.participants) - 1
    done_matches = []
    past_matches = []
    while play > 0:
        print("Round :", len(competition.participants) - play)
        playing_matches = []
        playing_players = []
        half = int(len(competition.participants)/2)
        for j in range(len(competition.participants)):
            try:
                n = j + int(half)
                duo = (competition.participants[j], competition.participants[n])    # half = IndexError
                reversed_duo = (competition.participants[n], competition.participants[j])
            except IndexError:
                n = j - int(half)
                duo = (competition.participants[j], competition.participants[n])    # half = IndexError
                reversed_duo = (competition.participants[n], competition.participants[j])
            if duo not in past_matches:
                # print("NOT") : Technique pour retrouver quelle branche a un problème
                playing_matches.append(duo)
                playing_players.append(competition.participants[j])
                playing_players.append(competition.participants[n])
                past_matches.append(duo)
                past_matches.append(reversed_duo)
                print("\n")
                display_match(duo)
            else:
                # print("OK") : Technique pour retrouver quelle branche a un problème
                for i in range(len(competition.participants)):
                    if j == i:
                        continue
                    if competition.participants[j] in playing_players:
                        continue
                    if competition.participants[i] in playing_players:
                        continue
                    temp_duo = (competition.participants[j], competition.participants[i])
                    if temp_duo in past_matches:
                        continue
                    temp_reversed_duo = (competition.participants[i], competition.participants[j])
                    if temp_reversed_duo in past_matches:
                        continue
                    playing_matches.append(temp_duo)
                    playing_players.append(competition.participants[j])
                    playing_players.append(competition.participants[i])
                    past_matches.append(temp_duo)
                    past_matches.append(temp_reversed_duo)
                    print("\n")
                    display_match(temp_duo)
                    break
        for duo in playing_matches:
            result = ask_result(duo, competition.participants)
            match = duo, result
            done_matches.append(match)
        competition.participants = points_update(competition.participants)
        play -= 1


def serialize_players(participants):
    serialized_players = []
    for i in range(len(participants)):
        temp_participant = participants[i]
        serialized_player = {
            'family_name': temp_participant.family_name,
            'firstname': temp_participant.firstname,
            'date_of_birth': temp_participant.date_of_birth,
            'gender': temp_participant.gender,
            'points': temp_participant.points}
        serialized_players.append(serialized_player)
    return serialized_players


def serialize_tournament(contest):
    serialized_tournament = {
        'name': contest.name,
        'place': contest.place,
        'date': contest.date,
        'round_number': contest.round_number,
        'time_control': contest.time_control,
        'description': contest.description}
    return serialized_tournament


player1 = Player("Feugueur", "Malik", "2000-03-13", "M", 0)
player2 = Player("Bulard", "Julien", "1992-05-27", "M", 0)
player3 = Player("Maukeur", "Feli", "1999-09-09", "F", 0)
player4 = Player("Juste", "Innome", "1990-11-06", "M", 0)
players = [player1, player2, player3, player4]

tournament = Tournament("CG-SENLIS", "Senlis", "2021-06-02", 3, players, "Bullet", "Tkt bg")

while True:
    print("MENU :")
    print("- CREER LES JOUEURS : 1")
    print("- AFFICHER LES JOUEURS : 2")
    print("- CREER LE TOURNOI : 3")
    print("- AFFICHER LE TOURNOI : 4")
    print("- AFFICHER LES PARTICIPANTS : 5")
    print("- LANCER LE TOURNOI : 6")
    print("- CREER LE FICHIER D'ARCHIVE : 7")
    print("- ARCHIVER LE TOURNOI : 8")
    print("- ARCHIVER LES PARTICIPANTS : 9")
    print("- QUITTER L'APPLICATION : 0")
    try:
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
            display_players(tournament.participants)
        elif Chiffre == 6:
            play_round(tournament)
        elif Chiffre == 7:
            db = TinyDB(input("Nom du fichier d'archive : ") + ".json")
            tournaments_table = db.table("tournament")
            tournaments_table.truncate()
            players_table = db.table("players")
            players_table.truncate()
        elif Chiffre == 8:
            tournaments_table.insert(serialize_tournament(tournament))
        elif Chiffre == 9:
            players_table.insert_multiple(serialize_players(tournament.participants))
        elif Chiffre == 0:
            break
    except ValueError:
        print("Veuillez choisir un chiffre disponible!")

# Remarque :
# - nom des variables (Anglais ou français !cohérence!)
# Fonction (Nommer ce qu'elle prend en types d'arguments et ce qu'elle sort en types)
