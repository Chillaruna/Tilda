"""Skriv en egen klass som representerar en plats.
Klassen ska ha attribut för alla data i filen.
Klassen ska ha metoderna __str__ och __init__
Du kan om du vill även ha en till klass som håller reda på platserna.
Utöver __str__ och __init__ ska du skriva minst tre metoder (medlemsfunktioner) sammanlagt (antingen i platsklassen eller den valfria klassen för alla platser).
Skriv en funktion som läser in data från filen, skapar objekt, och lagrar objekten i en lista. (lista = []).
Skriv ett program, uppdelat i lämpliga funktioner (eller metoder/medlemsfunktioner), där man kan söka i listan.
Vid redovisning ska du kunna förklara hur klasser/objekt/listor/filhantering fungerar i Python.
Betyg
betyg E:
Ditt program löser uppgiften
Ditt program uppfyller kraven för ett perfekt program
Du kan svara tillfredsställande på frågor om labben"""


print ("Hello World")

class Location(): #skriv en egen klass som representerar en plats

#klassen ska ha metoden __init__
    def __init__(self,namn,beskr,lat,lon,datum):
        self.name = name
        self.beskr = beskr
        self.lat = lat
        self.long = lon
        self.datum = datum
#kollade på föreläsning 2 och algoritm


#klassen ska ha metoden __str__
    def __str__(self):
        return self.namn



#Du kan om du vill även ha en till klass som håller reda på platserna.
class LocationPlace():


#en funktion som läser in data, skapar objekt, och lagrar objekten i en lista.
