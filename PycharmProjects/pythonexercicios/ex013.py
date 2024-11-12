sal=float(input("Qual é o salário do funcionário? R$"))
novo=sal+(sal*15/100)
print("Com 15% de aumento o funcionário que antes ganhava R${:.2f},passará a ganhar R${:.2f}".format(sal,novo))
