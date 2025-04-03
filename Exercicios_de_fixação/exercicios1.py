import random

# 1. Números primos
# Escreva um programa que recebe um número inteiro n do usuário e verifica se ele é primo.

def eh_primo(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 é o único número primo par
    
    # Se for par e diferente de 2, já não é primo
    if n % 2 == 0:
        return False

    # Testa apenas os ímpares de 3 até a raiz quadrada de n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
# Entrada do usuário
# num = int(input("Digite um número inteiro: "))

# Verifica e exibe o resultado
# if eh_primo(num):
#     print(f"{num} é um número primo.")
# else:
#     print(f"{num} não é um número primo.")


# 2. Palíndromo
# Peça ao usuário para digitar uma palavra e verifique se ela é um palíndromo (ou seja, se pode ser lida da mesma forma de trás para frente).



# 3. Soma de dígitos
# Crie um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos.

def numeros(n):

    print(sum(int(i) for i in (n)))

# numeros(input("Digite um numero para somarmos"))

# 4. Contagem de vogais e consoantes
# Solicite ao usuário uma frase e conte quantas vogais e quantas consoantes existem nela.

def contagem(n):
    vogal = 0
    consoante = 0
    
    for c in n:
        if c.isalpha() == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            vogal += 1
        
        else: consoante += 1

    print(f"Você tem {vogal} vogais e {consoante} consoante(s)")

# contagem(input("Digie uma palavra: ")) 

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
# adivinha()

# 7. Fatorial de um número
# Crie uma função que receba um número n e retorne o fatorial de n.

def fatorial(n1):
        cn1 = n1
        resultado = 1
        while cn1 > 0:
            resultado *= cn1
            cn1 -= 1
        print(f"o fatorial de {n1} é: {resultado}")
# fatorial(int(input("Digite um nunero: ")))

# 8. Fibonacci até N
# Peça ao usuário um número N e gere a sequência de Fibonacci até esse número.

def fibonacci():
    n = int(input("Digite um número N para gerar a sequência de Fibonacci até ele: "))
    
    # Inicializa os dois primeiros números da sequência
    a, b = 0, 1

    print("Sequência de Fibonacci:")
    while a <= n:
        print(a, end=" ")  # Imprime os valores na mesma linha
        a, b = b, a + b  # Atualiza os valores para o próximo termo

fibonacci()


# 9. Números pares e ímpares separados
# Peça ao usuário para inserir 10 números e armazene-os separadamente em listas de pares e ímpares.
#  No final, exiba as duas listas.

def par_impar():
    impar =[] #inicia uma lista vazia
    par = [] #inicia uma lista vazia
    contador = 0 #inicia um numero
    while contador != 10: #enquanto contador for diferente de 10 fica repetindo oque ta aqui dentro
            contador += 1 # contador recebe +1 agora contador é 1 na proxima repetição vai ser 2
            n1 = int(input("Digite um numero: ")) #recebe o numero  que o usuario escolheu
            if n1 % 2 == 0: #se o resto da divisão do numero que o usario escolheu for 0 a lista par recebe o numero do usuario
                par +=[n1]
            else: # se for qualquer numero diferente de 0 a lista impar recebe o numero
                impar +=[n1]
        #aqui acaba o codigo e volta a verificar se contador é diferente de 10
        
    print(f"Os numeros impares estão aqui {impar}\nAqui estão os pares{par}") #mostra uma mensagem com os numeros em cada lista depois que o contador chegou a 10

# par_impar()

# 10. Criptografia simples
# Peça ao usuário uma palavra e substitua cada vogal por um caractere *, exibindo a palavra modificada.

#DESAFIO EXTRA
# 📌 Desafio: Analisador de Textos para Digitação Rápida
# Imagine que você trabalha como desenvolvedor em uma empresa de cursos online, 
# e seu chefe pediu para você criar um analisador de dificuldade de digitação.

# Seu programa deve:

# Solicitar ao usuário um texto.
# # Contar quantas vogais e consoantes existem no texto.
# Medir o tamanho médio das palavras digitadas.
# Exibir um índice de dificuldade, baseado na quantidade de consoantes e no tamanho médio das palavras.
# 📊 Como calcular a dificuldade do texto?
# Fácil: Muitas vogais e palavras curtas (média ≤ 4 letras).
# Médio: Equilíbrio entre vogais/consoantes e palavras com 5-7 letras.
# Difícil: Muitas consoantes e palavras longas (média ≥ 8 letras).

def analisador(texto):
    vogal = "aeiouAEIOU"

    

