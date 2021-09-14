#!/usr/bin/env python
# -*- coding: utf-8 -*-

# question 1
def is_even_len(string: str) -> bool:

    longueur_chaine = len (string)
    longueur_chaine % 2 == 0
    if (longueur_chaine % 2 == 0):
        return True

    else:
        return False

        pass

#Question 2
def remove_third_char(string: str) -> str:
    chaine2 = (string [:2]+ string[3:])
    return chaine2

    pass


def replace_char(string: str, old_char: str, new_char: str) -> str:
    nouvelle_chaine = " "
    for lettre in string:
        if lettre == old_char:
            nouvelle_chaine += lettre
    return nouvelle_chaine
    pass


def get_number_of_char(string: str, char: str) -> int:
    rep = 0
    for letter in string:
        if letter == char:
            rep +=1

    return rep

    pass


def get_number_of_words(sentence: str, word: str) -> int:
    chaine = str.split(sentence)
    rep = 0
    for mot in chaine:
        if mot == word:
            rep+=1

    return rep

    pass


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
