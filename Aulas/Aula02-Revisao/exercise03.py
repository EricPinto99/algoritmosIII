notaA = float(input("Informe a primeira nota: "))
pesoNotaA = float(input("Informe seu peso: "))
notaB = float(input("Informe a segunda nota: "))
pesoNotaB = float(input("Informe seu peso: "))
notaC = float(input("Informe a terceira nota: "))
pesoNotaC = float(input("Informe seu peso: "))

def calcularMedia():
    somaPesos = pesoNotaA + pesoNotaB + pesoNotaC
    mediaPonderada = (notaA * pesoNotaA) + (notaB * pesoNotaB) / somaPesos
    return mediaPonderada

print("\nMedia Ponderada: %.2f" %calcularMedia())