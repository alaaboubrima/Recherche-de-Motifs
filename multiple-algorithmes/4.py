import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [103,110,120,124,126,136,151,166,175,183]
plt.plot(x_values, y_values)
plt.xlabel('La taille du motif')
plt.ylabel("Temps d'exécution (ms)")
plt.title("DURÉE D'EXÉCUTION DE RABIN-KARP ALGORITHME SELON LA LONGUEUR DES MOTIFS")
plt.show()