import time

def boyer_moore(T, M):
    n = len(T) # longueur du texte
    m = len(M) # longueur du motif

    # Construction du tableau d (dictionnaire)
    d = {} # dictionnaire pour stocker les décalages
    for j in range(m):
        for k in range(j):
            d[M[j]] = k
            #d[M[k]] = k
    R = [] # tableau résultat pour stocker les débuts d'occurrences du motif
    i = 0 # indice dans le texte
    s = 0 # indice dans le tableau résultat

    while i <= n - m :
        k = 0 # décalage en cas d'échec
        j = m - 1 # indice parcourant le motif à partir de la fin

        while j >= 0:
            if T[i + j] != M[j]: # caractères différents - échec
                if M[j] in d:
                    k = d[M[j]]
                else:
                    k = j + 1
                break
            j -= 1

        if k == 0: # on a trouvé une occurrence du motif
            R.append(i)
            s += 1
            k = 1
            i += 1
        else:
            i += k # déplacer la fenêtre dans le texte

    return R # retourner le tableau des débuts d'occurrences du motif



# Exemple d'utilisation :
T = "abc abc ab" # texte
M = "abc" # motif

# Début du chronomètre
start_time = time.time()

result = boyer_moore(T, M)

# Fin du chronomètre
end_time = time.time()

print("Débuts d'occurrences du motif dans le texte :")
print(result)

print("Temps écoulé : ", (end_time - start_time) * 1000000, " micro-sec")


