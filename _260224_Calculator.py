import math


class Calculator:
    def __init__(self):
        pass

    def sucet(self, a, b):
        return a + b

    def sucin(self, a, b):
        return a * b

    def delenie(self, a, b):
        return a / b

    def odvesna(self, c, b):
        return math.sqrt(c**2 - b**2)

    def korene_kvadratickej(self, a, b, c):
        determinant = math.sqrt(b**2 - 4*a*c)
        return [(-b - determinant)/(2*a), (-b + determinant)/(2*a)]


#---------------------------

choice = ""
calculator = Calculator()

print(" -- Kalkulacka --\nVyber si opperaciu ktoru chces na kalkulacke vykonat.\n")
print("Menu:")
print(" m -> pre zobrazenie menu")
print(" + -> pre scitavanie")
print(" * -> pre sucin")
print(" / -> pre delenie")
print(" odv -> pre vypocet dlzky odvesny v pravouhlom trojuholniku")
print(" kor -> pre vypocet korenov kvadratickej rovnice, (vysledok je pole s dvomi hodnotami)")


while True and choice != 'q':
    choice = input("Zadaj operaciu: ")

    if choice == 'm':
        print("Menu:")
        print(" m -> pre zobrazenie menu")
        print(" + -> pre scitavanie")
        print(" - -> pre odcitavanie")
        print(" / -> pre delenie")
        print(" odv -> pre vypocet dlzky odvesny v pravouhlom trojuholniku")
        print(" kor -> pre vypocet korenov kvadratickej rovnice, (vysledok je pole s dvomi hodnotami)")


    elif choice == '+':
        try:
            a = int(input("Prvy scitanec: "))
            b = int(input("Druhy scitanec: "))
        except ValueError:
            print("Musis zadat cislo!\n")

        answer = calculator.sucet()
        print(f"Odpoved: {answer}")


    elif choice == '*':
        try:
            a = int(input("Prvy scitanec: "))
            b = int(input("Druhy scitanec: "))
        except ValueError:
            print("Musis zadat cislo!\n")
        

        answer = calculator.sucin()
        print(f"Odpoved: {answer}")


    elif choice == '/':
        try:
            a = int(input("Delenec: "))
            b = int(input("Delitel: "))
        except ValueError:
            print("Musis zadat cislo!\n")


    elif choice == 'odv':
        pass


    elif choice == 'kor':
        pass


    else:
        print("Zadana operacia nebola rozpoznana.")

       