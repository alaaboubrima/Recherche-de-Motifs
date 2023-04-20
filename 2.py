import matplotlib.pyplot as plt

x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [90,105,110,124,155,156,160,161,161,167]
plt.plot(x_values, y_values)
plt.xlabel('La taille du motif')
plt.ylabel("Temps d'exécution (ms)")
plt.title("DURÉE D'EXÉCUTION D'AHO-CORASICK ALGORITHME SELON LA LONGUEUR DES MOTIFS")
plt.show()