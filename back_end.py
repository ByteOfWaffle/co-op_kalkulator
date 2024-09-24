## Funksjon for å legge sammen to tall
def leggSammen():
    tall1 = input("Skriv inn det første tallet: ")  
    tall2 = input("Skriv inn det andre tallet: ")   
    sum = int(tall1) + int(tall2)  # Tallene konverteres til heltall og legges sammen
    print(f'{tall1} + {tall2} = {sum}')  # Resultatet skrives ut

# Funksjon for å trekke fra to tall
def trekkFra():
    tall1 = input("Skriv inn det første tallet: ")  
    tall2 = input("Skriv inn det andre tallet: ")   
    diff = int(tall1) - int(tall2)  # Tallene konverteres til heltall og trekkes fra hverandre
    print(f'{tall1} - {tall2} = {diff}')  # Resultatet skrives ut

# Funksjon for å dele to tall
def dele():
    tall1 = input("Skriv inn det første tallet: ") 
    tall2 = input("Skriv inn det andre tallet: ")  
    diff = int(tall1) / int(tall2)  # Tallene konverteres til heltall og deles
    print(f'{tall1} / {tall2} = {diff}')  # Resultatet skrives ut

# Funksjon for å gange to tall
def gange():
    tall1 = input("Skriv inn det første tallet: ")  
    tall2 = input("Skriv inn det andre tallet: ")   
    diff = int(tall1) * int(tall2)  # Tallene konverteres til heltall og multipliseres
    print(f'{tall1} * {tall2}  = {diff}')  # Resultatet skrives ut

# Funksjon for å gange tre tall
def gange2():
    tall1 = input("Skriv inn det første tallet: ")  
    tall2 = input("Skriv inn det andre tallet: ")   
    tall3 = input("Skriv inn det tredje tallet: ")  
    diff = int(tall1) * int(tall2) * int(tall3)  # Tallene multipliseres
    print(f'{tall1} * {tall2} * {tall3}  = {diff}')  # Resultatet skrives ut

# Funksjon for å gange fire tall
def gange3():
    tall1 = input("Skriv inn det første tallet: ")  
    tall2 = input("Skriv inn det andre tallet: ")   
    tall3 = input("Skriv inn det tredje tallet: ")  
    tall4 = input("Skriv inn det fjerde tallet: ")  
    diff = int(tall1) * int(tall2) * int(tall3) * int(tall4)  # Tallene multipliseres
    print(f'{tall1} * {tall2} * {tall3} * {tall4}  = {diff}')  # Resultatet skrives ut

# Funksjon for å gange fem tall
def gange4():
    tall1 = input("Skriv inn det første tallet: ")  # Brukeren skriver inn første tall
    tall2 = input("Skriv inn det andre tallet: ")   # Brukeren skriver inn andre tall
    tall3 = input("Skriv inn det tredje tallet: ")  # Brukeren skriver inn tredje tall
    tall4 = input("Skriv inn det fjerde tallet: ")  # Brukeren skriver inn fjerde tall
    tall5 = input("Skriv inn det femte tallet: ")   # Brukeren skriver inn femte tall
    diff = int(tall1) * int(tall2) * int(tall3) * int(tall4) * int(tall5)  # Tallene multipliseres
    print(f'{tall1} * {tall2} * {tall3} * {tall4} * {tall5}  = {diff}')  # Resultatet skrives ut

def operator():
    def leggSammen(a, b):
        return a + b

    def trekkFra(a, b):
        return a - b

    def dele(a, b):
        return a / b if b != 0 else "Kan ikke dividere med null"

    def gange(a, b):
        return a * b

    operator_dict = {
        '+': leggSammen,
        '-': trekkFra,
        '/': dele,
        '*': gange
    }

    operator = input("Velg en operator (+, -, /, *): ")
    tall1 = int(input("Skriv inn første tall: "))
    tall2 = int(input("Skriv inn andre tall: "))
    

    if operator in operator_dict:
        result = operator_dict[operator](tall1, tall2)
        print(f"Resultat: {result}")
    else:
        print("ikke riktig operatør")