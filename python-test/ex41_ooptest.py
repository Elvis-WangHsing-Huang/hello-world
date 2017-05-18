import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

# a dictionary to map some python oo grammers to simple English
# key is a snippet
# value is a phrase
PHRASES = {
    "class %%%(%%%):":  #inheritance is-a
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\t\tdef __init__(self, ***)":
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\t\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attributes and set it to '***'."
}

# do they want to do drill phrases first?
if len(sys.argv) == 2 and sys.argv[1]=="english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
# urlopen(WORD_URL).readlines() # a list of str lines of the web document
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip()) # strip() remove heading and trailing white space


#print WORDS

def convert(snippet, phrase):
    # search "list comprehension" for the following expression
    # [mapping-expression for element in source-list if filter-expression]
    class_names = [w.capitalize() for w in
         random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3) # choose a random 1 ~ 3 parameters
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase: # (snippet, phrase)
        result = sentence[:] # copy the list of the sentence to result,
                             # result is a new list
                             # while if 'result = sentence', they will both point to the same list

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) # only replace once

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# Keep going until CTRL-D hit
try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question # exchnage => show phrase first

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye!"
