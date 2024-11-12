larg=float(input("Qual é a largura da pareder? "))
alt=float(input("Qual é a altura da parede? "))
area=larg * alt
print("Sua parede têm a dimensão de {}x{} e sua área é de {}m²".format(larg,alt,area))
tinta=area/2
print("Para pintar essa parede você vai precisar de {}L de tinta".format(tinta))
