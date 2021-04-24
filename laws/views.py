from django.shortcuts import render
from random import shuffle

from laws.models import Player

in_game_laws = []
roles = [
    "Fascista",
    "Hitler",
    "Liberal",
    "Liberal",
    "Liberal",
]


def homepage(request):
    return render(request, 'laws/index.html')


def how_is_how(request):
    data = {"players": Player.objects.all()}

    return render(request, 'laws/how_is_how.html', data)


def shuffle_players(request):
    players = Player.objects.all()
    shuffle(roles)

    for x in range(0, len(players), 1):
        temp = Player.objects.get(name=players[x].name)
        temp.role = roles[x]
        temp.save()

    return render(request, 'laws/shuffle_players.html')


def game(request):
    global in_game_laws
    data = {"num_of_laws": len(in_game_laws)}

    return render(request, 'laws/game.html', data)


def take_three(request):
    global in_game_laws
    laws_taken = []
    data = {}
    x = 0

    if len(in_game_laws) >= 3:
        while x < 3:
            laws_taken.append(in_game_laws.pop(0))
            x += 1
        data["laws_taken"] = laws_taken
        print(laws_taken)

    return render(request, 'laws/take_three.html', data)


def take_one(request):
    global in_game_laws
    data = {}

    if len(in_game_laws) >= 1:
        law = in_game_laws.pop(0)
        data["law"] = law
        print(law)

    return render(request, 'laws/take_one.html', data)


def cards_shuffle(request):
    global in_game_laws
    in_game_laws = [
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Fascista",
        "Liberal",
        "Liberal",
        "Liberal",
        "Liberal",
        "Liberal",
        "Liberal",
    ]
    shuffle(in_game_laws)

    return render(request, 'laws/cards_shuffle.html')

