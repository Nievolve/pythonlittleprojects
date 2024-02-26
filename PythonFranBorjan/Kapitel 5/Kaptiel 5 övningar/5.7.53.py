#Input variabel för personnummer
prsnr = "9008012934"
#Variabel som innehåller kontrolsiffran i en int
kontroll = int(prsnr[-2])
#Bool kontrol för kvinna/man
gender = False
#For-loop som kontrollerar om kontrollsiffran är jämn eller udda
for k in range(0,10,2):
    if k == kontroll:
        gender = True
#If sats som kollar den bool variabeln
if gender == True:

    print("Det är en tjej")
else:

    print("Det är en kille")