"""frase = "Curso em Video Python"
print(frase)"""
nome = str(input('Digite seu nome completo: '))

print('Seu nome em maiúsculas é: {}'.format(nome.upper()))

print('Seu nome em minúsculas é: {}'.format(nome.lower()))

print('Seu nome possui {} letras'.format(len(nome.replace(' ', ''))))

dividido = nome.split()

print('{} possui {} letras'.format(dividido[0], len(dividido[0])))