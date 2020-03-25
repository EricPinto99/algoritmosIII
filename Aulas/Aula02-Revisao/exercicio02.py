x = int(input("Informe o primeiro valor: "))
y = int(input("Informe o segundo valor: "))

def swap(x, y):
    x, y = y, x
    return x,y

print("\nBefore swap:\nx = %d and y = %d" %(x, y))

print("\nAfter swaping:\nx = %d and y = %d" %swap(x, y))