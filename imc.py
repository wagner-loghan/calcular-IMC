"""
Neste projeto, implementei um algoritmo para informar o IMC .
Onde é mostrado o peso e a altura, e é exibido a Indice de massa corporal.

"""

# Mostragem das classificaçoes

'''
IMC	               Categoria
abaixo de 16,00  - Baixo peso Grau III
16,00 a 16,99	 - Baixo peso Grau II
17,00 a 18.49	 - Baixo peso Grau I
18,50 a 24,99	 - Peso ideal
25,00 a 29,99	 - Sobrepeso
30,00 a 34,99	 - Obesidade Grau I
35,00 a 39,99	 - Obesidade Grau II
40,0 e acima	 - Obesidade Grau III
'''
altura = float(input("Digite sua altura em cm: "))
peso = float(input("Insira seu peso: "))
IMC = peso / (altura)**2


if IMC < 16.0:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Baixo peso Grau III')
elif IMC >=16.0 and IMC < 16.99:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Baixo peso Grau II')
elif IMC >=17.0 and IMC < 18.49:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Baixo peso Grau I')
elif IMC >=18.5 and IMC < 24.99:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Peso ideal')
elif IMC >=25.0 and IMC < 29.99:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Sobrepeso')
elif IMC >=30.0 and IMC < 34.99:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Obesidade Grau I')
elif IMC >=35.0 and IMC < 39.99:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Obesidade Grau II')
else:
    print(f'Seu IMC é de {IMC:.2f}, e é classificado como Obesidade Grau III')
    

