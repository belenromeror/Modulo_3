#Eliminando las vocales de una palabra

def delete_vowels(word):
    result = word
    vowels = ["a", "e","i","o","u"]
    for vowel in vowels:
        result = result.replace(vowel,"")
    return result

word = input("Ingresa una palabra ")
print (delete_vowels(word))