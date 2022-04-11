import json
from difflib import get_close_matches

data = json.load(open("data.json"))
# print(data["smog"])

## Now taking the input from the user to get the meaning of particular word

# word = input("Enter the word you want the meaning of: \n")
# output = data[word]
# print(output)

## We can print the same output as above in different way too using a function.

def translate(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.lower() in data:
        return data[word.lower()]

    elif word.upper() in data:
        return data[word.upper()]

    ## This Below elif will give us the suggestion for our entered word. For eg we entered supermann, then it will provide a suggestion that "Did You Mean Superman???" Sometimes in hurry we enter the wrong word than we get suggestion for the correct word, like we do during searching on google or any other browser. It is similar to that one. For this we have imported the get_close_matches method from difflib library.

    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s???" %get_close_matches(word, data.keys())[0])
        decide = input("Enter Y To Proceed, N To Not\n")
        if decide == "Y" or decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n" or decide == "N":
            return("You Opted Out As The Suggestion Provided Was Not Relevent")
        else:
            return("Wrong Input")

    else:
        print("Entered Word Is Not Present In Our Dictionary")

word = input("Enter the word you want the meaning of: \n")
output = translate(word)

## we have written below code for improving the interface of those words having more than 1 meaning
if type(output) == list:
    for item in output:
        print(item)
        # print("\n")
else:
    print(output)
    # print("\n")