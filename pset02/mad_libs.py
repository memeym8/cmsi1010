# ----------------------------------------------------------------------
# This is the file mad_libs.py

# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.

# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
# ----------------------------------------------------------------------

# Things to do:

# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!

# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.

# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.

# Here are some constraints:

#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.

templates = [
    {
        "text": "The :color :animal :action over the :adjective :plant.",
        "author": "Jack Dylan"
    },
    {
        "text": "The :adjective :place :action is where :person :verb.",
        "author": "Marty Klein"
    },
    {
        "text": ":character :verb as fast as he could to beat :noun in the :event.",
        "author": "Howard Harris"
    },
    {
        "text": "My favorite song is :song because I :verb the :adjective beat and the :adjective melody.",
        "author": "Enzo Davis"
    },
    {
        "text": "I :verb every morning because it makes me feel :feeling.",
        "author": "Xander Mark"
    },
    {
        "text": "The :color of the :noun is :color.",
        "author": "Matthew Meyer"
    },
    {
        "text": "We should :verb in the place because it would be :feeling",
        "author": "Matthew Meyer"
    },
    {
        "text": "The :color :food taste like :noun",
        "author": "Matthew Meyer"
    },
    {
        "text": "I am in love with :person because of their :adjective :bodypart and their :adjective :color :bodypart",
        "author": "Matthew Meyer"
    },
    {
        "text": "I feel :feeling after the :adjective :event",
        "author": "Matthew Meyer"
    }
]

  

import random

num = random.randint(0,9)
template = templates[num]['text']

words = template.split()

inputs = []

for word in words:
    if word[0] == ":":
        user_input = input(f"Give me a {word[1::]}: ")
        inputs.append(user_input)
    else:
        inputs.append(word)

print(' '.join(inputs))

yes_answers = {'yes', 'oui', 'sure'}

while True:
    response = input("Play again?")
    if response not in yes_answers:
        break   