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
    HTR.append((TS[0][1], TS[0][0], '', '-'))

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
text = "CACGTACGTACTA"
word = "ACG"
test = build_HTR(create_suffix_table(text))
# Créer un DataFrame Pandas à partir du tableau
df = pd.DataFrame(test, columns=['TS[i]', 'texte[TS[i]:]', 'lcp', 'HTR'])

# Afficher le DataFrame
print(df)