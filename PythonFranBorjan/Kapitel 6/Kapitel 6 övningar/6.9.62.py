#Skriv ett program som läser in ett antal tempertaurer som uppmätts vid samma tidpunkt på olika platser.
#Mätstationerna är numrerade från 1 och uppåt och programmet läser in temperaturerna i nummerordning(mätstation 1 osv).
#Programmet ska först skriva ut medelvärdet av alla temperaturerna.
#Det ska sedan skriva ut alla temperaturer som är högre än medelvärdet.
#För varje sådan tempertur ska programmet också skriva ut mätstationerns nummer.
lista_mätstation_temperatur =[]
lista_mätstation_nummer = []
mätstation_nummer = 1
while True:
    print("Skriv in temperatur på mätstation", mätstation_nummer, ". Avsluta med Q")
    mätstation_nummer += 1
    s = input(": ")
    if s.lower() == "q":
        mätstation_nummer -= 1
        break
    lista_mätstation_temperatur.append(int(s))
for x in range(1 , mätstation_nummer):
    lista_mätstation_nummer.append(x)
print(lista_mätstation_nummer)
print(lista_mätstation_temperatur)

#Beräkna medelvärde
medelvärde = 0
medelvärde_tot = 0
for x in lista_mätstation_temperatur:
    medelvärde += x
    medelvärde_tot = medelvärde/len(lista_mätstation_temperatur)

print("Medeltemperaturen är", medelvärde_tot, " grader")

ut_lista_medelvärde = []
ut_lista_stationer = []
count = 0
for x in  lista_mätstation_temperatur:
    count +=1
    if x > medelvärde_tot:
        ut_lista_medelvärde.append(x)
        ut_lista_stationer.append(count)
print("Lista på stationer över medeltemperaturen: ")
index_flyttare = 0
for x in ut_lista_stationer:
    print("Mätstation: ", x ,"  Temperaturen:  " , ut_lista_medelvärde[index_flyttare])
    index_flyttare +=1



