import matplotlib.pyplot as plt
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [98,105,124,124,136,145,151,170,175,175]
plt.plot(x_values, y_values)
plt.xlabel('Nombre de motifs')
plt.ylabel("Temps d'exécution (ms)")
plt.title("DURÉE D'EXÉCUTION DE COMMENTZ-WALTER ALGORITHME SELON LE NOMBRE DE MOTIFS")
plt.show()