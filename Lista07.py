#Faça um programa em Python utilizando o #for 
#(um programa pra cada um), que:
#Apresente os números de 1 a 100 (um por linha).
"""
for batata in range (1, 101, 1):
    print(batata)
"""
#Apresente os números de 100 a 1 (um por linha).
"""
for empanada in range (100,-1,-1):
    print(empanada)
"""    
#Apresente os números pares de 1 a 100 (um por linha).
"""
for pastel in range (1,101,1):
    if (pastel % 2 == 0):
        print (pastel)
"""
#Apresente os números ímpares de 1 a 100 (um por linha).
"""
for cocageladinha in range (1, 101, 1):
    if (cocageladinha % 2 !=0):
        print(cocageladinha)
"""
#Faça a soma dos números de 1 a 100 e ao final mostre apenas a soma total.
"""
x = 0
for y in range (x, 101):
    x=x+y
print(x)
"""
#Faça a soma dos números de X a Y (informados pelo usuário), desde que X seja menor que Y, e apresente o valor total (semelhante ao anterior).
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
#Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final.
# Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
j = int(input("Digite o valor do fatorial: "))
if(j == 0):
    print("O resultado é: ",1)
else:       
    for fatorial in range (1, j):
        j = j * fatorial 
    print (j)
