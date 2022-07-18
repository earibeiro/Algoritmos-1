#1) Faça algoritmos em Python, utilizando o while, que:
#a) Apresente na tela os números de 1 a 100.
"""
numeros = 1
while (numeros <=100):
    print(numeros)
    numeros +=1
"""

#b) Faça a soma dos números de 1 a 100 e apresente somente o resultado.
contador = 1
soma = 0
while(contador <=100):
    soma = soma + contador
print(soma)

#c) Apresente na tela somente os números pares entre 50 e 100.

#d) Apresente na tela somente os números ímpares entre 1 e 50.

#e) Apresente na tela somente a soma dos números pares entre 1 e 100.

#f) Apresente na tela os números de X a Y 
# (peça para o usuário informar os valores de X e de Y).

#g) Faça a soma dos números de X a Y e apresente somente o resultado
# (peça para o usuário informar os valores de X e de Y).

#h) Apresente na tela somente os números ímpares entre X e Y
# (peça para o usuário informar os valores de X e de Y).

#2) Faça um programa para calcular a tabuada:
#a) do 1 ao 10 para um número informado pelo usuário.

#b) do X ao Y para um número informado pelo usuário
# (o usuário também deve informar os valores de X e Y).

#3) Na matemática, o fatorial é um número natural 'n', representado por 'n!',
# é o produto de todos os inteiros positivos menores ou iguais a 'n'. Por exemplo:
# o fatorial de 5 é representado por 5! que é igual a 5x4x3x2x1. Fala um programa que
#  peça um número para o usuário e apresente na tela seu fatorial.

#4) Sendo 'H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N', faça um programa que peça ao
# usuário qual o termo final (N) e calcule o valor de H.
"""
n = int(input("Digite o termo final do cálculo: "))
contador = 1
h = 0
while (contador <= n):
    h = h + (1/contador)
    contador += 1
print(h)
"""

#Não é um exercício
"""
cont = 100
num = 0
while (cont > 0):
    if (cont%4 == 0):
        num+=1
    cont -= 1     
print(num)
"""

#5) Faça um programa em Python "Acertou, ganhou!" o programa deverá:
#a) Gerar um número aleatório entre 1 e 10 e pedir para o usuário digitar
# números até que acerte. Ao acertar, apresente uma mensagem parabenizando
# e finalize o programa.
"""
import random
aleatorio = random.randint(1, 10)
hit = int(input("Digite um número: "))
while (hit!=aleatorio):
    hit = int(input("Digite um número novamente: ))
print("Parabéns você acertou o número!")
"""

#b) Modifique o programa anterior para contar quantas vezes o usuário digita
# números tentando acertar. No final, mostra uma mensagem parabenizando ele
# e mostrando quantas tentativas ele teve para acertar o número.
"""
import random
aleatorio = random.randint(1, 10)
contagem = 0
hit = int(input("Digite um número: "))
while (hit != aleatorio):
    contagem +=1
    hit = int(input("Que pena, tente novamente \nDigite um número novamente: "))
print(f"Parabéns, você precisou de apenas {contagem+1} tentativas")    
"""

#c) Gerar um número aleatório entre 1 e 10 e pedir para o usuário digitar
# números até que acerte, porém a cada erro do usuário você deve gerar
# um número aleatório novamente. Ou seja, a cada rodada ele gera um número
# diferente que o usuário tem que acertar.
"""
import random
r = random.randint(1,10)
a = int(input("Tente acertar, digite um número: "))
while(a!=r):
    r = random.randint(1,10)
    a = int(input("Mais uma vez, digite um número: "))
print("Parabéns bacane!")    
"""

#d) Modifique o programa anterior para contar quantas vezes o usuário digita
# números tentando acertar. No final, mostre uma mensagem parabenizando ele e mostrando
# quantas tentativas ele teve para acertar o número.
"""
import random
r = random.randint(1, 10)
a = int(input("Tente acertar, digite um número: "))
conta = 0
while(a != r):
    r = random.randint(1, 10)
    a = int(input("Mais uma vez, digite um número: "))
    conta = conta +1
print(f"Parabéns bacane!Foram apenas {conta+1} tentativas")
"""

#6) Faça um programa que mostre o menu a seguir, receba a opção do usuário e 
# os dados necessários para executar cada operação. O programa será executado repetidamente
# até que o usuário passe o número informado para sair do programa (opção).
#== == == Menu Principal == == ==
#1. Par ou ímpar?
#2. Potência XY
#3. Raiz quadrada
#4. Sair
#Observação: Se o usuário informar uma opção inválida, apresente uma mensagem informando isso.
"""
import math
opt = 0
while (opt!=4):
    print("====== Menu Principal ======\n1. Par ou Ímpar?\n2. Potência X^Y\n3. Raiz quadrada\n4. Sair")
    opt = int(input("Digite a opção desejada: "))
    while (opt > 4 or opt < 1):
        print("Erro, as opções são entre 1 e 4!!!")
        opt = int(input("Digite a opção desejada: "))
    if (opt == 1):
        pi = int(input("Digite o número: "))
        if (pi%2 == 0):
            print("O número é par")
        else:
            print("O número é ímpar")
    elif (opt == 2):
        num = int(input("Digite o número da base: "))
        expo = int(input("Digite o valor do expoente: "))
        resu = math.pow(num,expo)
        print(f"\n{num}^{expo} = {resu}\n")
    elif (opt == 3):
        ra = int(input("Digite o valor: "))
        iz = math.sqrt(ra)
        print(f"A raíz quadrada de {ra} é {iz}")        
    else:
        print("Saindo...")
"""

#7) Faça um programa que mostre o menu a seguir, receba a opção do usuário e dos dados
# necessários para executar cada operação. O programa será executado repetidamente até
# que o usuário passe o número informado para sair do programa (opção).
"""
menu = 0
soma = 0
while (menu!=4):
    print("====== Menu Principal ======\n1. Fazer a tabuada do 1 ao 10 para um número X\n2. Apresentar os múltiplos de X entre 1 e 100\n3. Apresentar a soma dos números de 1 a 100\n4. Sair do programa")
    menu = int(input("Selecione a opção desejada do menu: "))
    while(menu > 4 or menu < 1):
        print("Erro")
        menu = int(input("Selecione a opção desejada do menu: "))
    if (menu == 1):
        tabu = int(input("Digite o número que você deseja ver a tabuada: "))
        for cont in range (1, 11):
            ada = tabu*cont
            print(f"{tabu} x {cont} = {ada}")
    elif (menu == 2):
        mult = int (input("Digite o número que deseja saber os múltiplos: "))
        for contador in range(1, 101):
            if(contador%mult==0):
                print(contador)
    elif (menu == 3):
        for cont in range (1,101,1):
            soma += cont
        print(soma)
        soma = 0
    else:
        print("Valeu, falou!")
"""

#8)
"""
cont = 0
opt = 1
while(opt!=0):
    cont += 1
    opt = int(input("Se desejar sair pressione 0, se não, outro número."))
    if (opt != 0):
        prod = float(input("Digite o valor do produto: "))
"""

#9) O departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
# que leia sete temperaturas, e informe ao final a menos e a maior temperatura, além da
# média das temperaturas.
"""
tempmax = -999999999999999999999999999999999
tempmin = 9999999999999999999999999999999999
print("Bem vindo ao programa de leitura de temperatuas")
temp = float(input("Digite a temperatura em graus celsius: "))
"""
    