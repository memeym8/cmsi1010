templates = [
    {
        "text": "The :color :animal :action over the :adjective :plant.",
        "author": "Jack Dylan",
    },
    {
        "text": "The :adjective :place :action is where :person :verb.",
        "author": "Marty Klein",
    },
    {
        "text": ":character :verb as fast as he could to beat :noun in the :event.",
        "author": "Howard Harris",
    },
    {
        "text": "My favorite song is :song because I :verb the :adjective beat and the :adjective melody.",
        "author": "Enzo Davis",
    },
    {
        "text": "I :verb every morning because it makes me feel :feeling.",
        "author": "Xander Mark",
    },
    {"text": "The :color of the :noun is :color.", "author": "Matthew Meyer"},
    {
        "text": "We should :verb in the place because it would be :feeling",
        "author": "Matthew Meyer",
    },
    {"text": "The :color :food taste like :noun", "author": "Matthew Meyer"},
    {
        "text": "I am in love with :person because of their :adjective :bodypart and their :adjective :color :bodypart",
        "author": "Matthew Meyer",
    },
    {"text": "I feel :feeling after the :adjective :event", "author": "Matthew Meyer"},
]


import random

num = random.randint(0, 9)
template = templates[num]["text"]

words = template.split()

inputs = []

for word in words:
    if word[0] == ":":
        user_input = input(f"Give me a {word[1::]}: ")
        inputs.append(user_input)
    else:
        inputs.append(word)

print(" ".join(inputs))

yes_answers = {"yes", "oui", "sure"}

while True:
    response = input("Play again?")
    if response not in yes_answers:
        break
