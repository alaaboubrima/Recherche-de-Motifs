# Programme Python pour l'implémentation de
# Algorithme Aho-Corasick pour la correspondance des chaînes

# defaultdict est utilisé uniquement pour stocker la sortie finale
# Nous renverrons un dictionnaire où key est le mot correspondant
# et la valeur est la liste des index du mot correspondant

import time
import matplotlib.pyplot as plt
from collections import defaultdict

# Les tableaux et les files d'attente ont été implémentés à l'aide de listes.

class AhoCorasick:
	def __init__(self, mots):

		# Nombre maximum d'états
        # doit être égal à la somme de la longueur de tous les mots-clés.
		self.max_states = sum([len(mot) for mot in mots])

		# Nombre maximal de caractères.
		self.max_characters = 26

        # LA FONCTION DE SORTIE EST IMPLÉMENTÉE EN UTILISANT []
        # Le bit i dans ce masque vaut 1 si le mot avec
        # index i apparaît lorsque la machine entre dans cet état.
        # Disons qu'un état produit deux mots "il" et "elle" et
        # dans notre liste de mots fournie, il a l'index 0 et elle a l'index 3
        # donc la valeur de out[state] pour cet état sera 1001
        # Il a été initialisé à tous les 0.
        # Nous avons pris un état supplémentaire pour la racine.
		self.out = [0]*(self.max_states+1)

		# LA FONCTION D'ÉCHEC EST IMPLÉMENTÉE EN UTILISANT fail []
        # Il y a une valeur pour chaque état + 1 pour la racine
        # Il a été initialisé à tous les -1
        # Cela contiendra la valeur de l'état d'échec pour chaque état
		self.fail = [-1]*(self.max_states+1)

		# LA FONCTION GOTO (OU TRIE) EST IMPLÉMENTÉE EN UTILISANT goto [[]]
        # Nombre de lignes = max_states + 1
        # Nombre de colonnes = max_characters soit 26 dans notre cas
        # Il a été initialisé à tous les -1.
		self.goto = [[-1]*self.max_characters for _ in range(self.max_states+1)]
		
		# Convertir tous les mots en minuscules
        # pour que notre recherche soit insensible à la casse
		for i in range(len(mots)):
		    mots[i] = mots[i].lower()
		
		# Tous les mots du dictionnaire qui seront utilisés pour créer Trie
        # L'indice de chaque mot-clé est important :
        # "out[state] & (1 << i)" est > 0 si nous venons de trouver mot[i]
        # dans le texte.
		self.mots = mots

		# Une fois le Trie construit, il contiendra le numéro
        # de nœuds dans Trie qui est le nombre total d'états requis <= max_states
		self.states_count = self.__build_matching_machine()


	# Construit la machine de correspondance de chaînes.
    # Renvoie le nombre d'états de la machine construite.
    # Les états sont numérotés de 0 jusqu'à la valeur de retour - 1, inclus.
	def __build_matching_machine(self):
		k = len(self.mots)

		# Au départ, nous avons juste l'état 0
		states = 1

		# Convalues pour la fonction goto, c'est-à-dire remplir goto
        # Cela revient à construire un Trie pour les mots[]
		for i in range(k):
			mot = self.mots[i]
			etat_current = 0

			# Traiter tous les caractères du mot courant
			for character in mot:
				ch = ord(character) - 97 # Ascii 'a' = 97

				# Allouer un nouveau nœud (créer un nouvel état)
                # si un noeud pour ch n'existe pas.
				if self.goto[etat_current][ch] == -1:
					self.goto[etat_current][ch] = states
					states += 1

				etat_current = self.goto[etat_current][ch]

			# Ajouter le mot actuel dans la fonction de sortie
			self.out[etat_current] |= (1<<i)

		# Pour tous les personnages qui n'ont pas
        # une arête depuis la racine (ou état 0) dans Trie,
		for ch in range(self.max_characters):
			if self.goto[0][ch] == -1:
				self.goto[0][ch] = 0
		
		# La fonction d'échec est calculée dans
        # largeur du premier ordre en utilisant une file d'attente
		queue = []

		# Itérer sur toutes les entrées possibles
		for ch in range(self.max_characters):

			# Tous les nœuds de profondeur 1 ont un échec
            # valeur de la fonction sous la forme 0. Par exemple,
            # dans le diagramme ci-dessus, nous passons à 0
            # des états 1 et 3.
			if self.goto[0][ch] != 0:
				self.fail[self.goto[0][ch]] = 0
				queue.append(self.goto[0][ch])

		# Maintenant, la file d'attente a les états 1 et 3
		while queue:

			# Supprimer l'état frontal de la file d'attente
			state = queue.pop(0)

			# Pour l'état supprimé, recherchez l'échec
            # fonction pour tous ces caractères
            # pour lequel la fonction goto n'est pas définie.
			for ch in range(self.max_characters):

				# Si la fonction goto est définie pour
                # caractère 'ch' et 'état'
				if self.goto[state][ch] != -1:

					# Trouver l'état d'échec de l'état supprimé
					echec = self.fail[state]

					# Trouver le nœud le plus profond étiqueté par propre
                    # suffixe de chaîne de la racine à l'état actuel.
					while self.goto[echec][ch] == -1:
						echec = self.fail[echec]
					
					echec = self.goto[echec][ch]
					self.fail[self.goto[state][ch]] = echec
                    # Fusionner les valeurs de sortie
					self.out[self.goto[state][ch]] |= self.out[echec]

					# Insérer le nœud de niveau suivant (de Trie) dans la file d'attente
					queue.append(self.goto[state][ch])
		
		return states



    # etat_current - L'état actuel doit être entre
    # 0 et le nombre d'états - 1.
    # input_suiv - Le prochain caractère qui entre dans la machine.
	def __find_next_state(self, etat_current, input_suiv):
		answer = etat_current
		ch = ord(input_suiv) - 97 # Ascii value of 'a' is 97

		# Si goto n'est pas défini, utilisez
        # fonction d'échec
		while self.goto[answer][ch] == -1:
			answer = self.fail[answer]

		return self.goto[answer][ch]


	# Cette fonction trouve toutes les occurrences de tous les mots dans le texte.
	def search_mots(self, text):
		# Convertir le texte en minuscules pour rendre la recherche insensible à la casse
		text = text.lower()

		# Initialiser etat_current à 0
		etat_current = 0

		# Un dictionnaire pour stocker le résultat.
		# La clé ici est le mot trouvé
		# La valeur est une liste de toutes les occurrences de l'index de début
		result = defaultdict(list)

		# Parcourir le texte à travers la machine construite
        # pour trouver toutes les occurrences de mots
		for i in range(len(text)):
			etat_current = self.__find_next_state(etat_current, text[i])

			# Si la correspondance n'est pas trouvée, passer à l'état suivant
			if self.out[etat_current] == 0: continue

			# Sinon, stockez le mot dans le dictionnaire de résultats
			for j in range(len(self.mots)):
				if (self.out[etat_current] & (1<<j)) > 0:
					mot = self.mots[j]

					# L'indice de début du mot est (i-len(mot)+1)
					result[mot].append(i-len(mot)+1)

		# Renvoyer le dictionnaire de résultat final
		return result

if __name__ == "__main__":
    # Début du chronomètre
    # start_time = time.time()
    
    with open('text/text.txt', 'r') as f:
        content = f.read()
        text = content

        # print("Distinct characters in the text:")
        # for char in distinct_chars:
        #     print(char)
        #distinct_chars = set(text)
	    

        # exemple simple

        # mots = ["Alice", "nothing", "hello", "nice", "seemed", "normal", "chapter", "he", "did", "end"]
        # aho_chorasick = AhoCorasick(mots)
        # result = aho_chorasick.search_mots(text)

        # for mot in result:
        #     for i in result[mot]:
        #         print("Le mot", mot, "apparaît de", i, "à", i+len(mot)-1)
                
        # # Fin du chronomètre
        # end_time = time.time()
        
        # print("Temps écoulé : ", (end_time - start_time) * 1000, " ms")




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
            aho_chorasick = AhoCorasick(mots[i][0:10])
            result = aho_chorasick.search_mots(text)
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

  
