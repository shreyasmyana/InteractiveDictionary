import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    if word in data:
        print("DEFINATION:-")
        for value in data[word]:
            print(value)
    else:
        print("Unable to find word. Do you mean:",get_close_matches(word,data.keys())[0])
        choice=input("YES / NO: ")
        if choice.lower()=="yes":
            translate(get_close_matches(word,data.keys())[0])
        else:
            print("Sorry try different word")


if __name__ == "__main__":

    word = input("Enter the word: ")
    translate(word)
