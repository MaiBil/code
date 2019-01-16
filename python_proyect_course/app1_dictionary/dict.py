import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def seek_def():
    word = input("Enter a word: ").lower()
    close_match = close_match = get_close_matches(word, data.keys(), cutoff=0.8)
    if word in data:
        return data[word]
    elif len(close_match) > 0:
        misspell = input(f"Did you mean {close_match[0]}? Y/N " ).upper()
        if misspell == "Y":
            return data[close_match[0]]
        else:
            return "That word does not exist!"
    else:
        return "That word does not exist!"


if __name__ == '__main__':
    output = seek_def()
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
