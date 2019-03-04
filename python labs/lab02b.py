#Madlib
print ("Welcome to Madlibs")
print()
import random
while True:
    adjectives = input("Give me 3 adjectives seperated by commas: ")
    raw_adj = adjectives.split(",")
    adj_list = raw_adj[:]
    random.shuffle(adj_list)
    if len(adj_list) != 3:
        print("not the right number of adjectives!")
        adjectives = input("Give me 3 adjectives seperated by commas: ")
    nouns = input('Give me 4 nouns seperated by commas: ')
    raw_nouns = nouns.split(",")
    noun_list = raw_nouns[:]
    random.shuffle(noun_list)
    if len(noun_list) != 4:
        print("not the right number of nouns!")
        nouns = input('Give me 4 nouns seperated by commas: n')
    verb1 = input( "Ok, how about one verb ending in -ing: ")
    story = f"{adj_list[0]} matters not. Look at me. Judge me by my {adj_list[1]}, do you? Hmm? Hmm. And well you should not. For my ally is the {noun_list[0]}, and a powerful ally it is. Life {verb1} it, makes it grow. Its {noun_list[1]} surrounds us and binds us. {adj_list[2]} beings are we, not this crude matter. You must feel the Force around you; between you, me, the {noun_list[2]}, the rock, everywhere. Yes, even between the land and the {noun_list[3]}."
    print()
    print(story)
    print()
    exit_string = input("Would you like to play again? Y/N:")
    if exit_string.upper() == "N":
        break