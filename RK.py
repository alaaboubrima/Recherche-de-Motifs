import time
import matplotlib.pyplot as plt

# Fonction de hachage 1
def hash_func1(pattern):
    # Utiliser une simple somme des codes ASCII des caractères comme fonction de hachage
    hash_val = 0
    for char in pattern:
        hash_val += ord(char)
    return hash_val

# Fonction de hachage 2
def hash_func2(pattern):
    # Utiliser une somme pondérée des codes ASCII des caractères comme fonction de hachage
    hash_val = 0
    weight = 1
    for char in pattern:
        hash_val += (ord(char) * weight)
        weight += 1
    return hash_val

# Fonction de hachage 3
def hash_func3(pattern):
    # Utiliser une multiplication des codes ASCII des caractères comme fonction de hachage
    hash_val = 1
    for char in pattern:
        hash_val *= ord(char)
    return hash_val

# Fonction d'ajout d'un motif dans les filtres de Bloom
def add_pattern_to_bloom_filters(pattern, bloom_filters):
    # Utiliser les trois fonctions de hachage pour ajouter le motif dans les trois filtres de Bloom
    bloom_filters[0].add(hash_func1(pattern))
    bloom_filters[1].add(hash_func2(pattern))
    bloom_filters[2].add(hash_func3(pattern))

# Fonction de recherche multiple avec l'algorithme de Rabin-Karp
def rabin_karp_multiple(text, patterns):
    # Créer les trois filtres de Bloom
    bloom_filters = [set(), set(), set()]

    # Ajouter les motifs dans les filtres de Bloom
    for pattern in patterns:
        add_pattern_to_bloom_filters(pattern, bloom_filters)

    # Liste pour stocker les motifs trouvés dans le texte
    found_patterns = []

    # Parcourir le texte avec une fenêtre de la même longueur que les motifs
    for i in range(len(text)):
        # Extraire la sous-chaîne de la fenêtre
        window = text[i:i+len(patterns[0])]

        # Vérifier si la fenêtre passe les trois filtres de Bloom
        pass_filters = True
        for j in range(3):
            if hash_func1(window) not in bloom_filters[0] or hash_func2(window) not in bloom_filters[1] or hash_func3(window) not in bloom_filters[2]:
                pass_filters = False
                break

        # Si la fenêtre passe les trois filtres de Bloom, vérifier si elle correspond à l'un des motifs
        if pass_filters:
            for pattern in patterns:
                if window == pattern:
                    found_patterns.append(pattern)

    # Retourner les motifs trouvés dans le texte
    return found_patterns

# # Exemple simple
# text = "abc wse cde zx"
# patterns = ["abc", "we", "cde", "zx"]
# found_patterns = rabin_karp_multiple(text, patterns)
# print("Motifs trouvés dans le texte :", found_patterns)










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

            rabin_karp_multiple(text, mots[0][0:i+1])
            
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