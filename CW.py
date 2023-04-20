import time
import matplotlib.pyplot as plt

def recherche(text, motif):
    # Fonction pour trouver le motif dans la chaîne de texte en utilisant
    # l'algorithme Commentz-Walter

    # Prétraiter la chaîne de motif pour créer la fonction d'échec
    echec = create_echec_fonction(motif)

    # Initialiser les pointeurs pour les chaînes de texte et de motif
    i = 0
    j = 0

    # Parcourir la chaîne de texte
    while i < len(text):

        # Vérifier si le caractère actuel de la chaîne de texte
        # correspond au caractère actuel de la chaîne de motif
        if text[i] == motif[j]:

            # Si les caractères correspondent, incrémenter les
            # pointeurs pour les deux chaînes
            i += 1
            j += 1

        # Si la chaîne de motif a été trouvée,
        # retourner l'indice de départ de la correspondance
        if j == len(motif):
            return i - j

        # Si le caractère actuel de la chaîne de texte
        # ne correspond pas au caractère actuel de la
        # chaîne de motif, utiliser la fonction d'échec pour
        # sauter une partie de la chaîne de texte qui ne peut
        # pas correspondre au motif
        if i < len(text) and text[i] != motif[j]:
            if j > 0:
                j = echec[j - 1]
            else:
                i += 1

    # Si la chaîne de motif n'a pas été trouvée
    # dans la chaîne de texte, retourner -1
    return -1


def create_echec_fonction(motif):
    # Fonction pour prétraiter la chaîne de motif
    # et créer la fonction d'échec
    echec = [0] * len(motif)

    # Initialiser les pointeurs pour la chaîne de motif
    i = 0
    j = 1

    # Parcourir la chaîne de motif
    while j < len(motif):

        # Si le caractère actuel de la chaîne de motif
        # correspond au caractère précédent,
        # incrémenter les pointeurs pour les deux chaînes
        if motif[i] == motif[j]:
            echec[j] = i + 1
            i += 1
            j += 1
        else:

            # Si les caractères ne correspondent pas, utiliser la
            # fonction d'échec pour sauter une partie de la chaîne
            # de motif qui ne peut pas correspondre à la chaîne de texte
            if i > 0:
                i = echec[i - 1]
            else:
                echec[j] = 0
                j += 1

    return echec

        # # exemple simple

        # # Chaîne de motif
        # motifs = ["ab", "cd"]

        # # Recherche du motif dans la chaîne de texte en utilisant
        # # l'algorithme Commentz-Walter
        # for motif in motifs:
        #     indice = recherche(text, motif)
        #     print(motif, "trouvé à l'indice", indice)

        # # Afficher le résultat
        # if indice < 0:
        #     print("motif not found in the text string")





with open('text/text2.txt', 'r') as f:
        content = f.read()
        text = content




        # construction du graphe
        x_values = []
        y_values = []
        # construction d'un tableau de 10 tableaux de 10 motifs 
        mots = [
		        ['my', 'he', 'yo', 'of', 'do', 'us', 'no', 'ok', 'hi', 'oh'],
                ['she', 'bee', 'dae', 'oil', 'kai', 'old', 'new', 'him', 'her', 'his'],
                ['alar', 'rock', 'slat', 'gaup', 'dhai', 'tanh', 'thro', 'rump', 'arar', 'pint'],
                ['jheel', 'bemat', 'chine', 'yourn', 'smoky', 'bebog', 'lamin', 'fitty', 'arise', 'trout'],
                ['acuity', 'vespid', 'reckon', 'coempt', 'hakeem', 'jinket', 'charge', 'usself', 'doddie', 'shasta'],
                ['punjabi', 'upsweep', 'bundook', 'wyandot', 'tittery', 'crinose', 'gloater', 'archsee', 'upshoot', 'koranic'],
                ['dirigent', 'coemploy', 'apicitis', 'yengeese', 'slothful', 'enquirer', 'retation', 'ballogan', 'devonian', 'babouche'],
                ['prompture', 'meandrous', 'plowlight', 'catkinate', 'violaceae', 'oxytropis', 'spongeous', 'unarrival', 'delegatee', 'whitetail'],
                ['saucerless', 'occultness', 'unalarming', 'pictorical', 'expectedly', 'plastidome', 'vialmaking', 'ostensibly', 'dispreader', 'zoological'],
                ['supernatant', 'borzicactus', 'thunderlike', 'purushartha', 'forniciform', 'prerailroad', 'collyweston', 'naggingness', 'uncongealed', 'lubritorian']                
		]
        for i in range(10):
            # Début du chronomètre
            start_time = time.time()

            indice = recherche(text, mots[0][0:i+1])
            
            # Fin du chronomètre
            end_time = time.time()
            x_values.append(i+1)
            y_values.append((end_time - start_time) * 1000)
            y_valuesINT = [int(x) for x in y_values]
            print(i, "Temps écoulé : ", y_valuesINT[i], " ms")
            
        plt.plot(x_values, y_valuesINT)
        plt.xlabel('Nombre de motifs')
        plt.ylabel("Temps d'exécution (ms)")
        plt.title("DURÉE D'EXÉCUTION D'AHO-CORASICK ALGORITHME SELON LE NOMBRE DE MOTIFS")
        plt.show()

  













