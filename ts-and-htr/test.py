import pandas as pd

def table_suffix(text):
    # Créer la table des suffixes à partir du texte donné
    suffix_table = []
    for i in range(len(text)):
        suffix_table.append((text[i:], i))
    suffix_table.sort()
    return suffix_table


def recherche_occurrences(T, M):
    exist = False
    n = len(T)
    TS = table_suffix(T) # table des suffixes triée
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
        lcp = ""
        htr = 0
        suffix1 = TS[i][0]
        suffix2 = TS[i - 1][0]
        while htr < len(suffix1) and htr < len(suffix2) and suffix1[htr] == suffix2[htr]:
            lcp += suffix1[htr]
            htr += 1
        if lcp == "":
            lcp ="\u03B5"
        HTR.append((TS[i][1], TS[i][0], lcp, htr))
    
    return HTR


def build_HTR_multiple(TS1, TS2):
    TS1 = [(t[0], t[1], 1) for t in (TS1)]
    TS2 = [(t[0], t[1], 2) for t in (TS2)]

    TS = TS1 + TS2
    TS.sort()
    print(TS)
    n = len(TS)
    HTR = []
    HTR.append((TS[0][0], TS[0][1], TS[0][2] , 0))

    for i in range(1, n):
        htr = 0
        suffix1 = TS[i][0]
        suffix2 = TS[i - 1][0]
        while htr < len(suffix1) and htr < len(suffix2) and suffix1[htr] == suffix2[htr]:
            htr += 1
        HTR.append((TS[i][0], TS[i][1], TS[i][2], htr))
    
    return HTR


# Exemple d'utilisation :
text = "GATAAGATTGATG"
word = "ACG"

# indice = []
# for suffixe, i in recherche_occurrences(text, word)[0]:
#     indice.append(i)
# if recherche_occurrences(text, word)[1] == True:
#     print(f"Le mot '{word}' a été trouvé à l'indice {indice}")
# else:
#     print(f"Le mot '{word}' n'a pas été trouvé dans le texte")

ts = table_suffix(text)
htr = build_HTR(ts)


# 4 - 1
le_max = max(i[3] for i in htr)
#print("le(s) plus long(s) facteur(s) répété(s) dans le texte : ", end=" ")
for i in htr:
    if i[3] == le_max:
        print(i[2], end = " ")
        

# 4 - 2
arr = []
for i in range(len(htr)-2):
    for j in range(len(htr[i+1][2])):
        if htr[i+1][2][0:j+1] == htr[i+2][2][0:j+1] and htr[i+1][2][0:j+1] not in arr:
            arr.append(htr[i+1][2][0:j+1])
#print("\nles facteurs qui se répètent au moins 3 fois : ", arr)


print(table_suffix(text))
def inverse_table_suffix(ts):
    its = [0] * len(ts)
    for i in range(len(ts)):
        its[ts[i][1]] = i
    return its
its = inverse_table_suffix(ts)
print(its)
#print(htr)



def lgCondidat(htr, its):
    lgC = [0] * len (htr)
    for i in range(len(htr)):
        if its[i] < len(htr) - 1:
            lgC[i] = 1 + max(htr[its[i]][3], htr[its[i]+1][3])
        # la derniere case
        else: 
            lgC[i] = 1 + htr[its[i]][3] 

    return lgC
lgC = lgCondidat(htr, its)

htr = [(t[0], t[1], t[2], t[3], its[i], lgC[i]) for i, t in enumerate(htr)]

def lgC_facts(text, htr):
    pcf = []
    for i in range(len(htr)):
        if i + htr[i][5] <= len(htr):
            pcf.append(text[i:i+htr[i][5]])
        else:
            pcf.append("-")
    return pcf


facts = lgC_facts(text, htr)

print(facts)

for i in range(len(facts) - 1):
    if len(facts[i]) <= len(facts[i+1]) or i == len(facts) - 2:
        print(facts[i])

def rep_super_maximale(htr):
    reps = []
    for i in htr:
        print(i[2])
    for i in range(1, len(htr)):
        super = True
        for j in range(1, len(htr)):
            if htr[i][2] != htr[j][2]:
                if htr[j][2].startswith(htr[i][2]) or htr[j][2].endswith(htr[i][2]):
                    super = False
        if super:
            reps.append(htr[i][2])
        reps = list(set(reps))
    return reps

print(rep_super_maximale(htr))


# Créer un DataFrame Pandas à partir du tableau
df = pd.DataFrame(htr, columns=['TS[i]', 'texte[TS[i]:]', 'lcp', 'HTR', 'ITS', 'lgC'])
# Afficher le DataFrame
print(df)


text1 = "bcabbcab"
text2 = "caabba"
text3 = "cbcabb"
ts1 = table_suffix(text1)
ts2 = table_suffix(text2)
htr2 = build_HTR_multiple(ts1, ts2)

df = pd.DataFrame(htr2, columns=['texte[TS[i]:]', 'TS[i]', 'Text', 'HTR'])
print(df)
# maxim = htr2[0][3]
# for i in range(htr2):
#     if htr2[i][3] > maxim and htr2[i+1][3] > maxim and htr[i][2] != htr[i+1][2]:
#         tab.append()
    
