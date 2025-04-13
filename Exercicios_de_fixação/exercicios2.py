import time
import random
# 1️⃣ Contagem Progressiva
# Peça ao usuário um número inteiro positivo n e exiba uma contagem de 1 até n.

# Exemplo:
# Entrada: 5
# Saída: 1 2 3 4 5

def contagem(n):
    n1 = 0
    while n1 < n:
        n1 += 1
        time.sleep(1)
        print(f"{n1}")

# contagem(int(input("Informe um numero para contagem:")))


# 2️⃣ Contagem Regressiva
# Solicite um número ao usuário e exiba uma contagem regressiva até 0.

# Exemplo:
# Entrada: 5
# Saída: 5 4 3 2 1 0

def regressiva(n):
    while n >= 0:
        print(n)
        n -= 1
        

# regressiva(int(input("Digite um numero para contarmos até 0: ")))


# 3️⃣ Soma dos N primeiros números
# Peça um número n e calcule a soma de todos os números de 1 até n.

# Exemplo:
# Entrada: 4
# Cálculo: 1 + 2 + 3 + 4 = 10
# Saída: A soma é 10

def calcule(n):
    x = 0
    cont = 0
    while cont < n:
         cont += 1
         print(x)
         x = x + cont
    
    print(f"a soma de todos os numeros que antecedem {n} é {x}.")

# calcule(int(input("Digite um numero: ")))

# 4️⃣ Adivinhe o Número
# O programa escolhe um número secreto entre 1 e 10. O usuário deve tentar adivinhar o número até acertar. No final, o programa exibe quantas tentativas foram necessárias.

def adivinha(n):
    geranum = random.randint(1, 10)
    tentativas = 0
    while n < 1 or n > 10:
            print("Por Favor Digite um numero: ")
            int(input("Por favor digite um numero de 1 a 10:\n"))

    while n != geranum:
         tentativas += 1
         print(f"{n} Não é o numero escolhido por min, tente denovo:")
         n = int(input())
    tentativas += 1
    print(f"Você acertou, depois de {tentativas} tentativas.")
# adivinha(int(input("Por favor digite um numero de 1 a 10:\n")))

# 5️⃣ Tabuada
# Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

# Exemplo:
# Entrada: 3
# Saída:

# python-repl
# Copiar
# Editar
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30



# 6️⃣ Contando Pares e Ímpares
# O programa deve pedir números ao usuário até que ele digite 0. No final, exiba quantos números pares e quantos números ímpares foram digitados.

def par_impar():
    n = -1
    par = 0
    impar =0
    while n != 0:
        n = int(input("Digite um numero, digite 0 quando quiser terminar: "))
        if n % 2 == 0:
               par += 1
        else: 
               impar += 1
    print(f"foram digitados {par} numeros par e {impar} numeros impares")

# par_impar()

# 7️⃣ Fatorial de um Número
# Solicite um número inteiro positivo n e calcule o fatorial de n.

# Exemplo:
# Entrada: 5
# Cálculo: 5! = 5 × 4 × 3 × 2 × 1 = 120
# Saída: O fatorial de 5 é 120

# 8️⃣ Média de Números
# Peça ao usuário para inserir uma quantidade indefinida de números e calcule a média. O processo deve parar quando o usuário digitar 0.

def media():
    n = -1
    c = 0
    s = 0
    
    while n != 0:
          n = int(input("Digite um numero, Digite 0 para parar:"))
          s += n
          c += 1
    resultado = s / (c - 1)
    print(F"a média dos numeros digitados é: {round(resultado)}")

# media()
          

# 9️⃣ Números Ímpares em um Intervalo
# Solicite dois números inteiros a e b e exiba todos os números ímpares entre a e b (inclusive).

def impares():
     n1 = int(input("Digite um numero: "))
     n2 = int(input("Digite outro numero: "))
     impar = []
     while n1 <= n2:
          if n1 % 2 == 1:
            impar.append(n1)
          n1 += 1
          
     print(impar)
impares()
               
# 🔟 Sequência de Fibonacci
# Peça ao usuário um número n e exiba os primeiros n termos da sequência de Fibonacci.

# Exemplo:
# Entrada: 6
# Saída: 0 1 1 2 3 5

# 1️⃣1️⃣ Número Invertido
# Peça um número inteiro positivo ao usuário e exiba esse número invertido.

# Exemplo:
# Entrada: 1234
# Saída: 4321

# 1️⃣2️⃣ Verificação de Palíndromo
# Peça ao usuário uma palavra ou número e verifique se é um palíndromo (ou seja, se pode ser lido da mesma forma de trás para frente).

# Exemplo:
# Entrada: radar
# Saída: "radar" é um palíndromo

# 1️⃣3️⃣ Potência de um Número
# Peça ao usuário dois números, base e expoente, e calcule o resultado de base^expoente.

# Exemplo:
# Entrada: 2 5
# Cálculo: 2⁵ = 32
# Saída: O resultado é 32

# 1️⃣4️⃣ Divisores de um Número
# Peça um número ao usuário e exiba todos os seus divisores.

# Exemplo:
# Entrada: 12
# Saída: 1, 2, 3, 4, 6, 12

# 1️⃣5️⃣ Número Perfeito
# Solicite um número ao usuário e verifique se ele é um número perfeito (um número cuja soma de seus divisores próprios é igual a ele mesmo).

# Exemplo:
# Entrada: 6
# Divisores próprios: 1, 2, 3
# Soma: 1 + 2 + 3 = 6
# Saída: 6 é um número perfeito

# 1️⃣6️⃣ Contagem de Dígitos
# Peça um número ao usuário e exiba quantos dígitos ele possui.

# Exemplo:
# Entrada: 9876
# Saída: O número 9876 tem 4 dígitos.

# 1️⃣7️⃣ Produto dos Dígitos
# Solicite um número inteiro positivo e calcule o produto de seus dígitos.

# Exemplo:
# Entrada: 1234
# Cálculo: 1 × 2 × 3 × 4 = 24
# Saída: O produto dos dígitos é 24

# 1️⃣8️⃣ Soma de Números Pares em um Intervalo
# Peça dois números a e b e calcule a soma de todos os números pares entre eles (inclusive).

# 1️⃣9️⃣ Contagem de Vogais em uma Palavra
# Peça ao usuário uma palavra e conte quantas vogais (a, e, i, o, u) existem nela.

# Exemplo:
# Entrada: "programação"
# Saída: Existem 5 vogais.

# 2️⃣0️⃣ Quadrado Mágico 3x3
# Solicite ao usuário 9 números e organize-os em uma matriz 3x3. Depois, verifique se a matriz forma um quadrado mágico (a soma de cada linha, coluna e diagonal deve ser a mesma).