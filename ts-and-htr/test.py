import pandas as pd

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

def build_HTR(TS):
    n = len(TS)
    HTR = []
    HTR.append((TS[0][1], TS[0][0], '', 0))

    for i in range(1, n):
        str = ""
        lcp = 0
        suffix1 = TS[i][0]
        suffix2 = TS[i - 1][0]
        while lcp < len(suffix1) and lcp < len(suffix2) and suffix1[lcp] == suffix2[lcp]:
            str += suffix1[lcp]
            lcp += 1
        if str == "":
            str ="\u03B5"
        HTR.append((TS[i][1], TS[i][0], str, lcp))
    
    return HTR


# Exemple d'utilisation :
text = "ACGACACGCG"
word = "ACG"

indice = []
for suffixe, i in recherche_occurrences(text, word)[0]:
    indice.append(i)
if recherche_occurrences(text, word)[1] == True:
    print(f"Le mot '{word}' a été trouvé à l'indice {indice}")
else:
    print(f"Le mot '{word}' n'a pas été trouvé dans le texte")


htr = build_HTR(create_suffix_table(text))
# Créer un DataFrame Pandas à partir du tableau
df = pd.DataFrame(htr, columns=['TS[i]', 'texte[TS[i]:]', 'lcp', 'HTR'])
# Afficher le DataFrame
print(df)

# 4 - 1
max = max(i[3] for i in htr)
print("le(s) plus long(s) facteur(s) répété(s) dans le texte : ", end=" ")
for i in htr:
    if i[3] == max:
        print(i[2], end = " ")
        

# 4 - 2
arr = []
for i in range(len(htr)-2):
    for j in range(len(htr[i+1][2])):
        if htr[i+1][2][0:j+1] == htr[i+2][2][0:j+1] and htr[i+1][2][0:j+1] not in arr:
            arr.append(htr[i+1][2][0:j+1])
print("\nles facteurs qui se répètent au moins 3 fois : ", arr)
