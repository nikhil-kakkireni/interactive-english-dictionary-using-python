import json
from difflib import get_close_matches

data=json.load(open("076 data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys(),cutoff=0.8)):
        yn =  input("Did you mean %s instead?\n Enter 'Y' if YES else 'N'"%get_close_matches(w,data.keys(),cutoff=0.8)[0])
        yn = yn.lower()
        if yn == "y":
            return translate(get_close_matches(w,data.keys(),cutoff=0.8)[0])
        elif yn == "n" :
            return "The word doesn't exist. Please check it.\n"
        else:
            return "We didn't understand your query.\n"

    else:
        return "The word doesn't exist. Please check it.\n"
word = input("Enter a word:")
output = translate(word)
if type(output)== list:
    for item in output:
        print(item)
else:
    print(output)