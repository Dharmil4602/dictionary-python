import json

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

    else:
        print("Entered Word Is Not Present In Our Dictionary")

word = input("Enter the word you want the meaning of: \n")
output = translate(word)
print(output)
