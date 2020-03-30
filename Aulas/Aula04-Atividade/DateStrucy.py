from datetime import date

class Controller:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def valida_data(self):
        self.valida = False
        # Meses com 31 dias
        if (self.month == 1 or self.month == 3 or self.month == 5 or \
            self.month == 7 or self.month == 8 or self.month == 10 \
            or self.month == 12):
            if (self.day <= 31):
                self.valida = True
        # Meses com 30 dias
        elif (self.month == 4 or self.month == 6 or self.month == 9 or \
              self.month == 11):
            if (self.day <= 30):
                self.valida = True

        return self.valida

    def verifica_ano_bissexto(self):
        self.verifica = False
        if (self.year %4==0 and self.year%100!=0) or (self.year%400==0):
            self.verifica = True
        return self.verifica

    def valida_data_pascoa(self):
        self.x = 24
        self.y = 5

        self.a = self.year % 19
        self.b = self.year % 4
        self.c = self.year % 7
        self.d = (19 * self.a + self.x) % 7
        self.e = (2 * self.b + 4 * self.c + 6 * self.d + self.y) % 7

        if((self.d + self.e) > 9):
            self.day = self.d + self.e - 9
            print("A páscoa será dia " % str(self.day) % "de Abril")
        else:
            self.day = self.d + self.e + 22
            print("A páscoa será dia " % str(self.day) % "de Março")

        return self.day

print("### Digite a Operacao desejada - 0 para Sair ###")
op = input("[1]Validar data\n[2]Verificar ano bissexto\n[3]Validar data da Páscoa\n")

while (op != "0"):
    if (op == '1'):
        day = int(input("Informe o dia: "))
        month = int(input("Informe o mês: "))
        year = int(input("Informe o ano: "))

        data = Controller(day, month, year)

        if (data.valida_data()):
            print("Data válida")
        else:
            print("Data inválida")

    elif (op == '2'):
        day = None
        month = None
        year = int(input("Informe o ano: "))

        data = Controller(day, month, year)

        if (data.verifica_ano_bissexto()):
            print("O ano informado é bissexto.")
        else:
            print("O ano informado não é bissexto.")


    elif(op == '3'):
        day = int(input("Informe a dia: "))
        month = int(input("Informe o mês: "))
        year = int(input("Informe o ano: "))

        data = Controller(day, month, year)

        data.valida_data_pascoa()


    elif (op != '1' or op != '2' or op != '3'):
        print("Opercao Invalida")

    print("-----------------------------")

    print("### Digite a Operacao desejada - 0 para Sair ###")
    op = input("[1]Validar data\n[2]Verificar ano bissexto\n[3]Validar data da Páscoa\n")


print("FIM DE PROGRAMA")