def create_suffix_table(text):
    # Créer la table des suffixes à partir du texte donné
    suffix_table = []
    for i in range(len(text)):
        suffix_table.append((text[i:], i))
    suffix_table.sort()
    return suffix_table


def recherche_occurrences(T, M):
    exist = False
    n = len(T)
    TS = create_suffix_table(T) # table des suffixes triée
    d, f = 0, n-1
    while d < f:
        milieu = (d + f) // 2
        if M <= T[TS[milieu][1]:]:
            f = milieu
        else:
            d = milieu + 1
    deb = d
    f = n - 1
    lg = len(M)
    while d < f:
        milieu = (d + f) // 2
        if M == T[TS[milieu][1]:TS[milieu][1]+lg]:
            exist = True
            d = milieu + 1
        else:
            f = milieu - 1
    fin = f
    return TS[deb:fin+1], exist


# Exemple d'utilisation :
text = "CACGTACGTACTA"
word = "ACG"
indice = []
for suffixe, i in recherche_occurrences(text, word)[0]:
    indice.append(i)
if recherche_occurrences(text, word)[1] == True:
    print(f"Le mot '{word}' a été trouvé à l'indice {indice}")
else:
    print(f"Le mot '{word}' n'a pas été trouvé dans le texte")
