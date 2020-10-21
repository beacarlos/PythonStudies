import json #Importando funcoes para converter arquivos json para python
from difflib import get_close_matches #Importando funcao para achar as palavras parecidas
data = json.load(open("original.json"))

word = input("Digite uma palavra que deseja buscar:\n")
# seems = get_close_matches(word, data.keys(), cutoff = 0.5)
# print(seems)

def translate(word):
    if(word in data):
        return data[word]
    elif(word.title() in data):
        return data[word.title()]
    elif(word.capitalize() in data):
        return data[word.capitalize()]
    elif(word.lower() in data):
        return data[word.lower()]
    elif(len(get_close_matches(word, data.keys())) > 0):
        print("Voce quis dizer %s" %get_close_matches(word, data.keys())[0])
        decide = input("Digite y para sim ou n para nao: ")
        if(decide == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif(decide == "n"):
            return print("Essa palavra não existe!")
        else:
            return print ("Voce digitou a palavra errada? Digite s para sim ou n para nao")
    else:
        print("Essa palavra não existe!")

vetTranslate = translate(word)
if(vetTranslate != None):
    for x in vetTranslate:
        print(x)