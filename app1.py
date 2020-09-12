import json
from difflib import get_close_matches
data = json.load(open('data.json', 'r'))


def translate(word):
    close = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif len(close) > 0:
        print(" Did you mean %s instead?" % close[0])
        ans = input("If Yes Enter Y, else N for No: ").lower()
        if ans == 'y':
            return data[close[0]]
        elif ans == 'n':
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry."

    else:
        return " The word doesn't exist. Please double check it"


word = input('Enter a word: ').lower()
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
