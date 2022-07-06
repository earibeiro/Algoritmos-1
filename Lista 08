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
