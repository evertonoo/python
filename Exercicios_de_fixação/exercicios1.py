import random

# 1. Números primos
# Escreva um programa que recebe um número inteiro n do usuário e verifica se ele é primo.

# 2. Palíndromo
# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).

# 3. Soma de dígitos
# Crie um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.

# 4. Contagem de vogais e consoantes
# Solicite ao usuário uma frase e conte quantas vogais e quantas consoantes existem nela.

# 5. Média de números
# O usuário deve inserir números continuamente até digitar 0. O programa então deve calcular a média dos números inseridos.

def calculo():
    numeros = []
    contador = 0
    a = 0
    
    while stop != 0:
        stop = int(input("Digite um numero: "))
        
        if stop != 0:
            contador += 1
            numeros += [stop]
            print(contador)
        else:
            for n in numeros:
                a += n
            resultado = a / contador
            print(resultado)

# calculo()

# 6. Adivinhação de número
# O computador deve gerar um número aleatório de 1 a 50. O usuário deve tentar adivinhar esse número
#  e o programa deve indicar se o palpite é maior ou menor que o número correto até que o jogador acerte.
def adivinha():

    n1 = random.randint(1,50)
    n2 = 0
    while n1 != n2:
        n2 = int(input("Escolha um numero de 1 a 50: "))
        
        if n2 < 0 or n2 > 50:
            print(f"Por favor {n2} não esta entre os numeros que te pedi, por favor digite novamente: ")
            n1 = int(input())
        elif n2 < n1:
            print(f"O numero {n2} é menor que meu numero:")
        elif n2 > n1:
            print(f"O numero {n2} é maior que meu numero:")
        else:
            print(f"Parabens meu numero era {n1} igual o seu {n2}")
adivinha()

# 7. Fatorial de um número
# Crie uma função que receba um número n e retorne o fatorial de n.

# 8. Fibonacci até N
# Peça ao usuário um número N e gere a sequência de Fibonacci até esse número.

# 9. Números pares e ímpares separados
# Peça ao usuário para inserir 10 números e armazene-os separadamente em listas de pares e ímpares. No final, exiba as duas listas.

# 10. Criptografia simples
# Peça ao usuário uma palavra e substitua cada vogal por um caractere *, exibindo a palavra modificada.

