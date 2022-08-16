#Algoritmos e Estrutura de Dados I 
#Vetores - Lista de Atividades de Introdução
#Não é para utilizar laços de repetição nos exercícios. Faça tudo “na mão”.

#1)Para cada conjunto de valores abaixo, escreva o código necessário para criar vetores:
#a) 0  4  9  18  27  41  65  88  121
aaa = [0,4,9,18,27,41,65,88,121]
#b) Rafael   Ayslan   Daniela   Frank
bbb = ["Rafael","Ayslan","Daniela","Frank"]
#c) 3290,90   128,50   85,90   789,31
ccc = [3290.90, 128.50, 85.90, 789.31]

#2)Considerando o vetor criado no exercício 1.a):
#a)Apresente na tela todos os valores do vetor.
print(f"{aaa}\n{bbb}\n{ccc}")
#b)Apresente na tela todos os valores do vetor em ordem invertida (de trás para frente).
print(f"{ccc}\n{bbb}\n{aaa}")

#3)Crie um vetor com 5 números inteiros de modo que o usuário do programa vá digitar esses valores.
#a)Apresente na tela todos os valores do vetor.
vetor0 = [0]*5
vetor0[0] = int(input("Digite o 1° número: "))
vetor0[1] = int(input("Digite o 2° número: "))
vetor0[2] = int(input("Digite o 3° número: "))
vetor0[3] = int(input("Digite o 4° número: "))
vetor0[4] = int(input("Digite o 5° número: "))
#b)Apresente na tela o dobro de todos os valores do vetor.
print(f"{vetor0[0]*2}\n{vetor0[1]*2}\n{vetor0[2]*2}\n{vetor0[3]*2}\n{vetor0[4]*2}")
#c)Apresente na tela a metade de todos os valores do vetor.
print(f"{vetor0[0]*(1/2)}\n{vetor0[1]*(1/2)}\n{vetor0[2]*(1/2)}\n{vetor0[3]*(1/2)}\n{vetor0[4]*(1/2)}")

#4)Crie um vetor de strings para armazenar quatro dados do usuário: nome completo, endereço, telefone e email.
#a)Apresente na tela, de maneira organizada, todos os dados do usuário, exemplo:
#Nome completo:     Rafael Zottesso
#Endereço:         Rua ABC, 123
#Telefone:         (99) 99999-9999
#E-mail:             rafael.zottesso@ifpr.edu.br
#Obs.: para dar esse “espaço” utilize o código da tabulação \t. Cada linha precisa de uma quantidade diferente de tabulação. Você pode colocar várias usando \t\t\t, por exemplo.
dados = [""]*4
dados[0] = input("Digite seu nome completo: ")
dados[1] = input("Digite seu endereço: ")
dados[2] = input("Digite seu número de telefone com ddd: ")
dados[3] = input("Digite seu endereço de e-mail: ")
print(f"Nome completo:\t{dados[0]}\nEndereço:\t{dados[1]}\nTelefone:\t{dados[2]}\nE-mail:\t\t{dados[3]}")


#5)Crie um vetor com 4 números decimais (ponto-flutuante) de modo que o usuário do programa vá digitar esses valores.
num = [0.0]*4
num[0] = float(input("Digite o 1° número: "))
num[1] = float(input("Digite o 2° número: "))
num[2] = float(input("Digite o 3° número: "))
num[3] = float(input("Digite o 4° número: "))
#a)Apresente na tela a soma de todos os valores.
soma = num[0]+num[1]+num[2]+num[3]
print(f"A soma de todos os números é: {soma}")
#b)Apresente na tela a média de todos os valores.
qtd = len(num)
media = soma/qtd
print(f"A média dos valores é {media}")
#c)Apresente na tela o produto (multiplicação) de todos os valores.
mult = num[0]*num[1]*num[2]*num[3]
print(f"O produto da multiplicação é {mult}")
#d)Apresente na tela somente quantos valores são maiores do que 1000.
qvmm = 0
if(num[0] > 1000):
    qvmm +=1
if(num[1] > 1000):
    qvmm +=1
if(num[2] > 1000):
    qvmm +=1
if(num[3] > 1000):
    qvmm +=1
print(f"Existem {qvmm} valores maiores que 1000.")
#e)Apresente na tela a quantidade de valores que são maiores do que zero.
qvmz = 0
if(num[0] > 0):
    qvmz = qvmz+1
if(num[1] > 0):
    qvmz = qvmz+1
if(num[2] > 0):
    qvmz = qvmz+1
if(num[3] > 0):
    qvmz = qvmz+1
print(f"Existem {qvmz} valores maiores que zero.")
#f)Apresente na tela somente o maior valor do vetor.
maior = 0
if(num[0]>num[1] and num[0]>num[2] and num[0]>num[3]):
    print(f"O maior número é {num[0]}")
    maior=num[0]
if(num[1]>num[0] and num[1]>num[2] and num[1]>num[3]):
    print(f"O maior número é {num[1]}")
    maior=num[1]
if(num[2]>num[0] and num[2]>num[1] and num[2]>num[3]):
    print(f"O maior número é {num[2]}")
    maior=num[2]
if(num[3]>num[0] and num[3]>num[1] and num[3]>num[2]):
    print(f"O maior número é {num[3]}")
    maior=num[3]
#g)Apresenta na tela somente o índice do maior valor do vetor.
vet = [" "]*4
vet[0] = "0"
vet[1] = "1"
vet[2] = "2"
vet[3] = "3"
if(maior==num[0]):
    print(f"O índice {vet[0]} possui o maior valor")
if(maior==num[1]):
    print(f"O índice {vet[1]} possui o maior valor")
if(maior==num[2]):
    print(f"O índice {vet[2]} possui o maior valor")
if(maior==num[3]):
    print(f"O índice {vet[3]} possui o maior valor")
#h)Apresente na tela somente o menor valor do vetor.
menor = 0
if(num[0]<num[1] and num[0]<num[2] and num[0]<num[3]):
    print(f"O menor número é {num[0]}")
    menor=num[0]
if(num[1]<num[0] and num[1]<num[2] and num[1]<num[3]):
    print(f"O menor número é {num[1]}")
    menor=num[1]
if(num[2]<num[0] and num[2]<num[1] and num[2]<num[3]):
    print(f"O menor número é {num[2]}")
    menor=num[2]
if(num[3]<num[0] and num[3]<num[1] and num[3]<num[2]):
    print(f"O menor número é {num[3]}")
    menor=num[3]
#i)Apresenta na tela somente o índice do menor valor do vetor.
if(menor==num[0]):
    print(f"O índice {vet[0]} possui o menor valor")
if(menor==num[1]):
    print(f"O índice {vet[1]} possui o menor valor")
if(menor==num[2]):
    print(f"O índice {vet[2]} possui o menor valor")
if(menor==num[3]):
    print(f"O índice {vet[3]} possui o menor valor")
