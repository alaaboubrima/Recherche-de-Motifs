# 1. Construire sa table des suffixes TS et l’afficher
def table_suffix(text):
    # Créer la table des suffixes à partir du texte donné
    suffix_table = []
    for i in range(len(text)):
        suffix_table.append((text[i:], i))
    suffix_table.sort()
    return suffix_table


# 2. Rechercher un motif M dans le texte à l’aide de la table des suffixes TS
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


# 3. Construire la table HTR de T et l’afficher en montrant à chaque fois le préfixe commun entre deux suffixes consécutifs
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


# 4. A l'aide des tables TS et HTR, trouver et afficher
# - le(s) plus long(s) facteur(s) répété(s) dans le texte
# - les facteurs qui se répètent au moins 3 fois.
le_max = max(i[3] for i in htr)
print("le(s) plus long(s) facteur(s) répété(s) dans le texte : ", end=" ")
for i in htr:
    if i[3] == le_max:
        print(i[2], end = " ")
                

        # 4 - 2
arr = []
for i in range(len(htr)-2):
    for j in range(len(htr[i+1][2])):
        if htr[i+1][2][0:j+1] == htr[i+2][2][0:j+1] and htr[i+1][2][0:j+1] not in arr:
            arr.append(htr[i+1][2][0:j+1])
print("\nles facteurs qui se répètent au moins 3 fois : ", arr)


# 5. Construire l'inverse ITS de la table des suffixes de T et l’afficher
def inverse_table_suffix(ts):
            its = [0] * len(ts)
            for i in range(len(ts)):
                its[ts[i][1]] = i
            return its


# 6. Déterminer les plus courts facteurs uniques du texte en construisant la table LgCandidat.
# Rappel : un plus court facteur unique est un facteur unique u (qui apparaît une seule fois dans le texte)
# tel que tous ses facteurs propres (≠ u) sont des répétitions.
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

print("Tous les facteurs", facts)
print("Les plus courts facteurs uniques du texte")
for i in range(len(facts) - 1):
    if len(facts[i]) <= len(facts[i+1]) or i == len(facts) - 2:
        print(facts[i])


# 7. Déterminer les répétitions super-maximales du texte.
# Rappel : une répétition super-maximale est un facteur répété qui n'est facteur propre d'aucune autre
# répétition.
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


# 8. A l’aide des structures TS et HTR, retrouver le plus long facteur commun entre deux textes T1 et T2.
def plus_long(htr):
            paires_consecutives = []
            for i in range(len(htr)-1):
                if htr[i][2] != htr[i+1][2]:
                    paires_consecutives.append((htr[i+1][3], i+1))
                    # le i pour sauvgarder l'indice ou on a trouver cette paire

            paires_consecutives = sorted(paires_consecutives, reverse=True)
            
            # paires_consecutives[0][1] contient l'indice du plus long fact dans la table HTR car il est triee
            plus_long_fact = [paires_consecutives[0][1]]
            # cette boucle pour le cas ou on a plus q'un seul fact commun
            for i in range(len(paires_consecutives)-1):
                if paires_consecutives[i+1][0] == paires_consecutives[i][0]:
                    plus_long_fact.append(paires_consecutives[i+1][1])
                else:
                    break
            facts = []
            for i in plus_long_fact:
                facts.append((i, htr[i][0][0:htr[i][3]]))
            return sorted(facts)

text1 = "bcabbcab"
text2 = "caabba"


ts1 = table_suffix(text1)
ts2 = table_suffix(text2)


htr2 = build_HTR_multiple(ts1, ts2)

print(f"les plus long facteurs communs entre '{text1}' et '{text2}' sont {plus_long(htr2)}")