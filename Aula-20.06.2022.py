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
"""
conta = 0
for calc in range (0,6):
    x = float(input("Digite o {}° número: ".format(calc)))
    conta = conta + x
print("O resultado é: ",conta)
"""
"""
h = 0
n = int(input("Digite o termo final: "))
n = n+1
for banana in range (1,n):
    h = h + 1/banana
print(h)
"""
"""
import sys
soma = 0
vari2 = 0
y = -sys.maxsize-1
z = sys.maxsize

for raspadinha in range (1,7):
    
    x = int(input(f"Digite o {raspadinha}° número: "))
    if (y<x):
        y = x
    if(z>x):
        z = x
    if(x%2 == 0):
        soma = soma+1 #soma += 1
    else:
        vari2 = vari2+1 #vari2 += 1

print(f"Você digitou {soma} pares")
print(f"Você digitou {vari2} ímpares")
print(f"O menor número é {z}")
print(f"O maior número é {y}")
"""

"""
i = 0
while (i < 6):
    print(i)
    i += 1
"""
"""
inicio = 0

while(inicio <= 10):
    
    if (inicio%3 == 0):
        print(inicio)

    inicio += 1
"""
#Faça um programa para calcular a tabuada:
#do 1 ao 10 para um número informado pelo usuário.
#do X ao Y para um número informado pelo usuário
#(o usuário também deve informar os valores de X e Y).
"""
tabu = int(input("Digite número que deseja saber a tabuada: "))
oito = 1
while (oito <= 10):
    ada = tabu*oito
    print(f"{tabu} X {oito} = {ada}")
    oito += 1
"""
"""
usu = int(input("Qual tabuada você deseja saber? "))
inicio = int(input("Qual o inicio do intervalo? "))
fim = int(input("Qual o final do intervalo? "))

while(inicio <= fim):
    calc = usu*inicio
    print(f"{inicio} X {fim} = {calc}")
    inicio = inicio+1
"""
#Na matemática, o fatorial de um número natural n, representado por n!, 
# é o produto de todos os inteiros positivos menores ou iguais a n. 
# Por exemplo: o fatorial de 5 é representado por 5! que é igual a 5 x 4 x 3 x 2 x 1. 
# Faça um programa que peça um número para o usuário
#  e apresente na tela seu fatorial.
"""

bora = int(input("Digite o fatorial desejado: "))
termina = 1
while(bora > 0):
    termina = termina*bora
    print(termina)
    bora -= 1

"""
#Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que 
# peça ao usuário qual o termo final (N) e calcule o valor de H.
"""
finicio = 0
n = int(input("Digite o termo final: "))
h = 0

while(finicio <= n):
    if (finicio > 0):
        h = h + (1/finicio)
    finicio += 1
print(h)
"""
