# A program that prints popular computer games sorted alphabetically and numbered, using a while loop.

computer_games = [
    "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
    "League of Legends", "Valorant", "Grand Theft Auto V",
    "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

# sorted() is a built-in function that returns a new, sorted list
sorted_games = sorted(computer_games)

i = 0
while i < len(sorted_games):
    print(i + 1, sorted_games[i])
    i += 1
