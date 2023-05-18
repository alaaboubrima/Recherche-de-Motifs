import pandas as pd

""" 
1. Construire sa table des suffixes TS et l'afficher
"""
def table_suffix(text):
    # Créer la table des suffixes à partir du texte donné
    suffix_table = []
    for i in range(len(text)):
        suffix_table.append((text[i:], i))
    suffix_table.sort()
    return suffix_table

"""
Invers table suffix
"""
def inverse_table_suffix(ts):
            its = [0] * len(ts)
            for i in range(len(ts)):
                its[ts[i][1]] = i
            return its

"""
2. Rechercher un motif M dans le texte à l'aide de la table des suffixes TS
"""
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


"""
3. Construire la table HTR de T et l'afficher en montrant à chaque fois le préfixe commun entre deux
suffixes consécutifs
"""
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

"""
Construire la table HTR de deux texts T1, T2
"""
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

text = "abracadabra"
word = "abra"
ts = table_suffix(text)
its = inverse_table_suffix(ts)
htr = build_HTR(ts)

while True:
    user_input = input("Choisir entre 1 et 8 pour repondre au question, sinon 'q' pour quitter \n")

    if user_input == "q":
        break  # Exit the loop if the user enters 'q'

    if user_input == "1":
        
        df = pd.DataFrame(table_suffix(text), columns=['texte[TS[i]:]', 'TS[i]'])
        print(df)
    elif user_input == "2":
        indice = []
        for suffixe, i in recherche_occurrences(text, word)[0]:
            indice.append(i)
        if recherche_occurrences(text, word)[1] == True:
            print(f"Le mot '{word}' a été trouvé à l'indice {indice}")
        else:
            print(f"Le mot '{word}' n'a pas été trouvé dans le texte")
    elif user_input == "3":
        ts = table_suffix(text)
        htr = build_HTR(ts)
        # Créer un DataFrame Pandas à partir du tableau
        df = pd.DataFrame(htr, columns=['TS[i]', 'texte[TS[i]:]', 'lcp', 'HTR'])
        # Afficher le DataFrame
        print(df)





        """
        4. A l'aide des tables TS et HTR, trouver et afficher
        - le(s) plus long(s) facteur(s) répété(s) dans le texte
        - les facteurs qui se répètent au moins 3 fois. 
        """
    elif user_input == "4":
        # 4 - 1
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



        """
        5. Construire l'inverse ITS de la table des suffixes de T et l'afficher 
        """
    elif user_input == "5":
        def inverse_table_suffix(ts):
            its = [0] * len(ts)
            for i in range(len(ts)):
                its[ts[i][1]] = i
            return its
        its = inverse_table_suffix(ts)
        df = pd.DataFrame(its, columns=['ITS[i]'])
        print(df)
        




        """
        6. Déterminer les plus courts facteurs uniques du texte en construisant la table LgCandidat. 
        """
    elif user_input == "6":
        
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
        df = pd.DataFrame(htr, columns=['TS[i]', 'texte[TS[i]:]', 'lcp', 'HTR', 'ITS', 'lgC'])
        # Afficher la table HTR avec its et lgCondidat 
        print(df)

        print("Tous les facteurs", facts)
        print("Les plus courts facteurs uniques du texte")
        for i in range(len(facts) - 1):
            if len(facts[i]) <= len(facts[i+1]) or i == len(facts) - 2:
                print(facts[i])
        pass
    elif user_input == "7":
        """
        7. Déterminer les répétitions super-maximales du texte. 
        """
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

    elif user_input == "8":
        """
        8. A l'aide des structures TS et HTR, retrouver le plus long facteur commun entre deux textes T1 et T2.
        """
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
        text3 = "a-b-cd-ef-gh"
        text4 = "a.b.cd.ef.gh"

        ts1 = table_suffix(text1)
        ts2 = table_suffix(text2)
        ts3 = table_suffix(text3)
        ts4 = table_suffix(text4)
        
        htr2 = build_HTR_multiple(ts1, ts2)
        htr3 = build_HTR_multiple(ts3, ts4)

        print(f"les plus long facteurs communs entre '{text1}' et '{text2}' sont {plus_long(htr2)}")
        print(f"les plus long facteurs communs entre '{text3}' et '{text4}' sont {plus_long(htr3)}")
        pass
    else:
        print("Entree invalide. Veuillez entrer un nombre entre 1 et 8.")

print("Quitter le programme")

ts = table_suffix(text)
htr = build_HTR(ts)











