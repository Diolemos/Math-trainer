print("Welcome")

operator = input("Type: '1' for multiplication or,\nType '2' for division  ")


game_mode = input("Chose a game mode\nType '1' for Quiz or '2' for Endless")


def quiz_mode(operator=operator):
    pass


def endless_mode(operator=operator):
    pass


if game_mode == 1:
    quiz_mode()
elif game_mode == 2:
    endless_mode()
else:
    print("Invalid option")        