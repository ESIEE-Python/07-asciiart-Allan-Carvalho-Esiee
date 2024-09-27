#### Imports et définition des variables globales


#### Fonctions secondaires
'''
author : allan.carvalho@edu.esiee.fr
'''

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne
       de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    L=[]
    count = 1
    caractere = s[0]
    for i in range (1,len(s)) :
        if s[i]==caractere :
            count+=1
        else :
            L.append((caractere,count))
            caractere = s[i]
            count=1
    L.append((caractere,count))
    return L

def artcode_r(s):
    """retourne la liste de tuples encodant une 
       chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    count = 1
    tuple1 = (s[0], count)
    while count < len(s) and s[count] == s[0]:
        count += 1

    return [tuple1] + artcode_r(s[count:])


#### Fonction principale


def main():
    '''
    Test la fonction
    '''
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
