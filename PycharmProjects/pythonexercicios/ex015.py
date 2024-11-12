dia = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos Km o carro rodou? "))
soma = (dia * 60) + (km * 0.15)
print("O total a pagar é de R${:.2f}".format(soma))
