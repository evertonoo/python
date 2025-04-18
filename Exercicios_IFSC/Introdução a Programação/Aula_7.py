# 1. Verificando Se um Número é Positivo, Negativo ou Zero
# Crie um programa que solicita um número ao usuário e verifica se ele é positivo, negativo
# ou zero.

def verifica_numero():
    n = float(input("Digite um número: "))

    if n > 0:
        print("O numero que escolheu é positivo")
    elif n == 0:
        print("O numero é 0")
    else: 
        print("Seu número é um número negativo")
# verifica_numero()

# 2. Calculadora Simples
# Crie um programa que pede ao usuário dois números e uma operação (+, -, *, /) e realiza o
# cálculo correspondente.

def calculadora():
    n1 = float(input("Digite um numero para calcular: "))
    n2 = float(input("Digite outro numero para calcular: "))
    print(f"Escolha um operador\n1 para somar\n2 para subtrair\n3 para multiplicar\n4 para dividir ")
    operador = int(input("Digite o operador escolhido:\n"))
   
    
    if operador == 1:
        print(f"A soma de {n1} + {n2} é {n1 + n2}.")
    elif operador == 2:
        print(f"A subtração de {n1} + {n2} é {n1 - n2}.")
    elif operador == 3:
        print(f"A multiplicação de {n1} + {n2} é {n1 * n2}.")
    elif operador == 4:
        print(f"A divisão de {n1} + {n2} é {n1 / n2}.")
    else: print("Operação selecionada incorreta!")

# calculadora()

# 3. Classificação de Idade
# Crie um programa que classifica a idade de uma pessoa em:
# ● Criança: 0 a 12 anos
# ● Adolescente: 13 a 17 anos
# ● Adulto: 18 a 59 anos
# ● Idoso: 60 anos ou mais

def idade():
    idade = int(input("Qual sua idade: "))
    if idade <= 12:
        print("Criança:")
    elif idade > 12 and idade <= 17:
        print("Adolescente:")
    elif idade > 17 and idade <= 59:
        print("Adulto:")
    else:
        print("Idoso: ")
# idade()

# 4. Verificação de Par ou Ímpar
# Crie um programa que pede ao usuário para digitar um número inteiro e informa se ele é par
# ou ímpar.
def par_impar():
    n1 = int(input("Digite um número: "))
    if n1 % 2 == 0:
        print("Seu número é par")
    else: print("Seu número é impar")
# par_impar()

# 5. Maior de Três Números
# Peça ao usuário para digitar três números diferentes e mostre qual deles é o maior.
def maior_3():
    n1 = int(input("Digite um numero: "))
    n2 = int(input("Digite um numero: "))
    n3 = int(input("Digite um numero: "))

    if n1 > n2 or n1 > n3:
        print(f"{n1} é o maior dos números")
    elif n2 > n3:
        print(f"{n2} é o maior número")
    else: print(f"{n3} é o maior dos números")
# maior_3()


# 6. Verificação de Ano Bissexto
# Solicite ao usuário um ano e verifique se ele é bissexto.
# Dica: um ano é bissexto se for divisível por 4, mas não por 100, exceto se for divisível por 400.

def bissexto():
    ano = int(input("Digite o ano em que nasceu: "))
    if ano % 4 == 0 or ano % 400 == 0:
        print("O ano era bissexto")
    else:
        print("O ano não era bissexto")
# bissexto()

# 7. Aprovado ou Reprovado
# Peça ao usuário para digitar três notas de um aluno (de 0 a 10), calcule a média.
# ● Se a média for maior ou igual a 6, mostre a média e a palavra "Aprovado".
# ● Senão, mostre a média e a palavra "Reprovado".
# ● Se a média não estiver no intervalo válido, exiba "Nota inválida".

def resultados():
    nota1 = float(input("Insira a 1ª nota do aluno: "))
    nota2 = float(input("Insira a 2ª nota do aluno: "))
    nota3 = float(input("Insira a 3ª nota do aluno: "))

    media = (nota1 + nota2 + nota3) / 3

    if media >= 6 and media <= 10:
        print("Aluno Aprovado:")
    elif media < 6 and media >= 0:
        print("Aluno Reprovado")
    else:
        print("Nota inválida")
# resultados()

# 8. Sistema de Login Simples
# Crie um programa que simula um sistema de login simples.
# ● O usuário deve digitar um nome de usuário e uma senha.
# ● Verifique se o nome de usuário é "admin" e a senha é "1234".
# ○ Se ambos estiverem corretos, exiba: "Login bem-sucedido!"
# ○ Se o nome de usuário estiver errado, exiba: "Usuário inválido!"
# ○ Se a senha estiver errada, exiba: "Senha incorreta!"

def login():
    login = input("Usuario: ")
    senha = input("Senha: ")

    if login == "admin" and senha == "1234":
        print("LOGIN BEM SUCEDIDO")
    elif login != "admin" and senha == "1234":
        print("Usuario inválido")
    elif login == "admin" and senha != "1234":
        print("Senha incorreta!")
#login()


# 9. Cálculo do IMC e Classificação
# Crie um programa que pede ao usuário seu peso (em kg) e sua altura (em metros).
# O programa deve calcular o IMC usando a fórmula:
# IMC = peso / (altura ** 2)
# Depois, o programa deve classificar o resultado de acordo com a tabela abaixo:
# IMC Classificação
# Abaixo de 18.5 Abaixo do peso
# De 18.5 até 24.9 Peso normal
# De 25.0 até 29.9 Sobrepeso
# De 30.0 até 39.9 Obesidade
# Acima de 40.0 Obesidade grave

def imc():
    peso = float(input("Qual seu peso em KG? "))
    altura = float(input("Qual sua altura em Metros"))
    imc = peso / (altura ** 2)
    if imc <= 18.5:
        print("Abaixo do peso")
    elif imc > 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc > 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc > 30 and imc <= 39.9:
        print("Obesidade")
    else:
        print("Obesidade grave")

# imc()


# 10. Classificação de Triângulo
# Peça ao usuário os três lados de um triângulo e classifique-o como:
# ● Equilátero (três lados iguais),
# ● Isósceles (dois lados iguais),
# ● Escaleno (três lados diferentes).
# Dica: antes de classificar, verifique se os lados formam um triângulo válido.

def triangulo():
    l1 = int(input("Digite o 1º lado: "))
    l2 = int(input("Digite o 2º lado: "))
    l3 = int(input("Digite o 3º lado: "))

    if l3 > (l1 + l2) or l2 > (l1 + l3) or l1 > (l3 + l2):
        print("Medias não formam um triangulo")

    else: 
        if l1 == l2 and l1 == l3:
            print("Três lados iguais Equilátero")
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print("Dois lados iguais Isóceles")
        else:
            print("Três lados diferentes.")

triangulo()