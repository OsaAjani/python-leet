import random
def to_leet (phrase) :
    replacements = [
        ['o', 0],
        ['O', 0],
        ['i', 1],
        ['I', 1],
        ['z', 2],
        ['Z', 2],
        ['e', 3],
        ['E', 3],
        ['a', 4],
        ['A', 4],
        ['s', 5],
        ['S', '$'],
        ['t', 7],        
        ['T', 7],        
        ['B', 8],
    ]

    for replacement in replacements :
        if random.choice([True,False]) :
            phrase = phrase.replace(replacement[0], str(replacement[1]))


    return phrase
