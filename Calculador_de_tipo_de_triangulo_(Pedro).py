# Criação das Variáveis
a = 0.0
b = 0.0
c = 0.0

triangulo = ""

# Entrada dos Dados
nome = input("Digite seu nome: ")
a = float(input("Digite o tamanho em cm do lado A: "))
b = float(input("Digite o tamanho em cm do lado B: "))
c = float(input("Digite o tamanho em cm do lado C: "))
          
# Cálculos
if a == b or a == c or b == c:
    triangulo = "ISÓSCELES"
if a != b and b != c:
    triangulo = "ESCALENO"
if a == b and b == c:
    triangulo = "EQUILÁTERO"

# Resultado
print(f"{nome} o seu triangulo é {triangulo}")
