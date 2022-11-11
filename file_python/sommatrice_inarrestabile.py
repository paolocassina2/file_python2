#Esercizio 005: Sommatrice Inarrestabile
#Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
lista=[2,2,2,2,2,2]
somma=0
for x in lista:
	somma+=x
print(somma)

################################àà
#Esercizio 010: Generatore di Istogrammi
#Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

#Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

#***

#*******

#*********

#*****
lista2=[3, 7, 9, 5]
for x in lista2:
	print(x*"*")
