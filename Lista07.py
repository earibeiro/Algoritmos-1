#1. Faça um programa em Python utilizando o #for 
#(um programa pra cada um), que:

#a) Apresente os números de 1 a 100 (um por linha).
"""
for batata in range (1, 101, 1):
    print(batata)
"""
#b) Apresente os números de 100 a 1 (um por linha).
"""
for empanada in range (100,-1,-1):
    print(empanada)
"""    
#c) Apresente os números pares de 1 a 100 (um por linha).
"""
for pastel in range (1,101,1):
    if (pastel % 2 == 0):
        print (pastel)
"""
#d) Apresente os números ímpares de 1 a 100 (um por linha).
"""
for cocageladinha in range (1, 101, 1):
    if (cocageladinha % 2 !=0):
        print(cocageladinha)
"""
#e) Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.
"""
x = 0
for y in range (x, 101):
    x=x+y
print(x)
"""
#f) Faça a soma dos números de X a Y (informados pelo usuário), desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).
#Solução 1
"""
print ("Vamos somar os números entre o intervalo que você indicar!")
x = int(input("Digite o valor inicial: "))
y = int(input("Digite o valor final: "))
y = y+1
if (x > y):
    print("Erro. O segundo valor deve ser superior ao primeiro.")
    y = int(input("Digite o valor final: "))
for c in range (x, y):
    x = x + c
print ("O somatório total é igual a: ",x-1)                
"""
#Solução 2
"""
x = int(input("Digite valor inicial: "))
y = int(input("Digite o valor final: "))
y = y+1
if (x >= y):
    while (x >= y):
        print("Erro. o primeiro valor deve ser inferior ao segundo")
        x = int(input("Digite o valor inicial: "))
        y = int(input("Digite o valor final: "))
        y = y+1
for contagem in range (x,y, 1):
    x = x + contagem
print("O resultado total é: ", x-1)
"""
#g) Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final.
# Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
"""
j = int(input("Digite o valor do fatorial: "))
j = j + 1     
for fatorial in range (0, j):
    j = j * fatorial 
print (j)
"""
"""
x = 5
fat = 1
for cont in range (x, 0, -1):
    fat = cont*fat
print(fat)
"""
#2. Faça um programa que leia 5 números e informe apenas o maior número.
"""
num1 = 0
for maior in range (1, 6):
    num2 = int(input("Digite o {}° valor: ".format(maior)))
    if (num2 > num1):
        num1 = num2
print(num1)
"""
#3. Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
num1 = 0
for media in range (1, 6):
    num2 = int(input("Digite o {}° valor: ".format(media)))
    num1 = num1+num2
print("A soma dos valores corresponde a {} e a média é igual a {}".format(num1,num1/5))
"""
#4. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
for impares in range (1,51):
    if(impares%2 !=0):
        print(impares)
"""
#5. O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de
#10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele
#desenvolveu uma tabela que contém o número de itens que o cliente comprou e ao 
#lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar 
#quantos itens o cliente está levando e olhar na tabela de preços. Você foi 
#contratado para desenvolver o programa que monta esta tabela de preços, que
#conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
"""
print ("Lojas Quase Dois - Tabela de preços")
for preco in range (1, 51):
    num = 1.99*preco
    print("{} produto = R$ {} reais".format(preco,num))
"""
#6. Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do 1 ao 10 para um número informado pelo usuário.
"""
print("Vamos calcular a tabuada, meu jovem!")
num = int(input("Digite o número que você deseja ver a tabuada: "))
for tabuada in range (1, 11):
    num1 = num*tabuada
    print("{} x {} = {}".format(num,tabuada,num1))
"""
#7. Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do 
# X a Y para um número informado pelo usuário (semelhante ao anterior, porém o 
#usuário precisa informar três números).

#Possivel solução 1
"""
num3 = int(input("Digite qual o número que você quer ver a tabuada: "))
num1 = int(input("Digite em qual número você quer iniciar a tabuada: "))
num2 = int(input("Digite em qual número você quer terminar a tabuada: "))
if (num1 > num2):
    num1 = int(input("Digite em qual número você quer iniciar a tabuada: "))
    num2 = int(input("Digite em qual número você quer terminar a tabuada: "))
num2 = num2+1
for conta in range (num1, num2):
    num4 = num3*conta
    print("{} x {} = {}".format(num3,conta,num4))
"""
#Possivel solução 2
"""
num1 = int(input("Digite a primeira tabuada: "))
num2 = int(input("Digite a segunda tabuada: "))
num3 = int(input("Digite a terceira tabuada: "))
for tabuada in range (1, 11):
    num4 = num1*tabuada
    print("{} x {} = {}".format(num1,tabuada,num4))
print("---------------------------")
for tabuada in range (1, 11):
    num4 = num2*tabuada
    print("{} x {} = {}".format(num2,tabuada,num4))
print("---------------------------")
for tabuada in range (1, 11):
    num4 = num3*tabuada
    print("{} x {} = {}".format(num3,tabuada,num4))
"""
#Possível solução 3 - tabuadas que vão seguem um intervalo. Ex: 1, 2 e 3. Tabuada do 1, do 2 e do 3.
"""
inicio = int(input("Digite a primeira tabuada do intervalo: "))
for meio in range (1,11):
    fim = inicio*meio
    print("{} x {} = {}".format(inicio, meio, fim))
print("-------------------")
inicio = inicio+1
for meio in range(1,11):
    fim = inicio*meio
    print("{} x {} = {}".format(inicio, meio, fim))
print("-------------------")
inicio = inicio+1
for meio in range (1,11):
    fim = inicio*meio
    print("{} x {} = {}".format(inicio, meio, fim))
"""

#Exercício 12: Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
#utilizando laço de repetição (for ou while) que leia 10 temperaturas para calcular e informar na tela:
# a menor temperatura
# a maior temperatura
# a média das temperaturas
"""
bigtemp = 0
lowtemp = 100
avgtemp = 0
for temps in range (1,11):
    temperatura = float(input("Digite a temperatura: "))
    avgtemp = avgtemp + temperatura
    if (bigtemp < temperatura):
        bigtemp = temperatura
    if (lowtemp > temperatura):
        lowtemp = temperatura
print("A menor temperatura registrada foi {}°, a maior temperatura foi {}° e a média de {}°".format(lowtemp,bigtemp,avgtemp/10))
"""
#Exercício 13: Considerando a fórmula abaixo para calcular o valor de H, faça um programa 
#que peça ao usuário qual o termo final (N) e calcule o valor de H:
#H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
"""
h = 0
n = int(input("Digite o termo final: "))
n = n+1
for banana in range (1,n):
    h = h + 1/banana
print(h)
"""

#Exercício de aula do dia 2022.06.28
soma = 0
vari2 = 0
y = 0
z = 10000

for raspadinha in range (1,7):
    x = int(input(f"Digite o {raspadinha}° número: "))
    x = str(x)
    if (len(x) > 4):
        print("Erro!")
        x = float(input(f"Digite o {raspadinha}° número: "))
    x = int(x)
    if (y<x):
        y = x

    if(z>x):
        z = x

    if(x%2 == 0):
        soma = soma+1

    else:
        vari2 = vari2+1

print(f"Você digitou {soma} pares")
print(f"Você digitou {vari2} ímpares")
print(f"O menor número é {z}")
print(f"O maior número é {y}")


