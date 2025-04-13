def declara_variavel():
    nome = "Everton Vieira"
    idade = 34
    altura = 1.73
    estudante = True

    print("Nome: ",nome)
    print(f"Idade: {idade}")
    print(f"Altura: {altura}\nEstudante: {estudante}")

# declara_variavel() 

def converter_temperatura():
    celsius = float(input("Informe a temperatura em graus celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"A temperatura de {celsius} Graus Celsius em Fahrenheint é: {fahrenheit} Graus Fahrenheit.")

# converter_temperatura()

def pi():
    raio = float(input("Digite o raio do círculo"))
    pi = 3.14159
    area = pi * raio ** 2
    print(f"A área do cirulo é: {area}")

# pi()

# 💸 1) Dividindo a conta com taxa de serviço
# Um grupo de amigos foram a um restaurante e decidiram dividir igualmente o valor da
# conta, que inclui uma taxa de serviço de 10%. Escreva um programa que leia a quantidade
# de pessoas, o valor da conta sem a taxa, calcule e mostre o valor da taxa, o valor total com a
# taxa, e quanto cada pessoa deve pagar.

def dividir_conta():
    qtdPessoas = int(input("Quantas pessoas são? "))
    valorConta = float(input("Qual foi o valor da conta? "))
    taxa = valorConta * 0.1
    contaTaxa =  valorConta + taxa
    contaDividida = contaTaxa / qtdPessoas
    print(f"A conta teve R$ {taxa} de taxa, totalizando R$ {contaTaxa}, vai ficar R$ {contaDividida} para cada.")
# dividir_conta()

# ⛽ 2) Custo da viagem
# Você viajou uma certa distância e quer calcular quanto gastou em combustível.
# Considerando que você já conhece o consumo médio do seu veículo, escreva um programa
# que leia:
# ● A distância percorrida (em km);
# ● O consumo médio do carro (km por litro);
# ● O preço do litro do combustível.
# O programa deve calcular:
# ● Quantos litros foram gastos;
# ● O custo total da viagem

def consumo_combustivel():
    distancia = float(input("Quantos KM você percorreu? "))
    media = float(input("Qual a média que seu veiculo faz? "))
    precoCombustivel = float(input("Qual o valor do litro de combústivel: "))
    consumo  = distancia  / media
    print(f"Foram gastos {consumo} litros de combústivel, tendo um custo total de viagem R$ {round(consumo * precoCombustivel)}.00")

# consumo_combustivel()

# 🎁 3) Compras com desconto e frete
# Maria está comprando presentes pela internet. Cada presente custa o mesmo valor, e ela
# recebeu um desconto de 5% sobre o valor total da compra. Além disso, há um frete fixo de
# R$ 20,00. Escreva um programa que leia:
# ● O valor de um presente;
# ● A quantidade de presentes.
# Calcule:
# ● O valor total com desconto;
# ● O valor final com o frete incluído.


def frete():
    valorPresente = float(input("Qual o valor do presente? "))
    qtdPresentes = int(input("Quantos presentes vai enviar? "))

    total = valorPresente * qtdPresentes * 0.5
    totalFrete = total  + 20

    input(f"O valor da sua compra com desconto é R${total:.2f}, com o frete fica R$ {totalFrete:.2f}.")
# frete()    



# 🎓 1) Verificando Aprovação em um Exame
# Para ser aprovado em um exame, o estudante precisa ter uma nota média maior ou igual a
# 7.0 e uma frequência maior ou igual a 75%. Solicite os dados do usuário e verifique se ele
# foi aprovado.

def media():
    notas = []
    media = 0
    while len(notas) < 5:
       nota = float(input("Digite a nota do aluno: "))
       notas.append(nota)
    
    for n in notas:
        media += n
    resultado = media / len(notas)
    faltas = int(input("Quantas faltas o aluno teve? "))

    if resultado < 7 or faltas > 25:
        print("Aluno reprovado")
    else: 
        print("Aluno aprovado! ")
# media()

# 🛍 2) Oferta Especial
# Uma loja oferece um desconto se o cliente comprar mais de 10 itens ou se o valor total da
# compra for superior a R$100. Solicite os dados do usuário e verifique se ele tem direito ao
# desconto.

def desconto():
    item = -1
    itens = []
    while item != 0:
        item = float(input("Digite o valor do item, ou 0 para sair: "))
        itens.append(item)
    
    if sum(itens) > 100 or len(itens) - 1 > 10:
        print("Parabêns vocês esta apto para o desconto")
    else: print(f"total R$ {sum(itens)}")


# desconto()



# ️ 3) Calculadora de IMC
# O Índice de Massa Corporal (IMC) é uma medida usada para avaliar se uma pessoa está
# dentro do peso ideal. Ele é calculado dividindo o peso (em kg) pela altura (em metros)
# elevada ao quadrado. Verifique se a pessoa está com o IMC entre 18.5 e 24.9, que é
# considerado o intervalo do peso ideal.

def imc():
    peso = float(input("Qual seu peso? "))
    altura = float(input("Qual sua altura? "))
    calculo = (peso / altura**2) 

    if calculo < 18.5:
        print("Magreza")
    elif calculo > 18.5 and calculo < 24.9:
        print("Normal")
    elif calculo > 25 and calculo < 29.9:
        print("Sobrepeso")
    elif calculo >30 and calculo < 39.9:
        print("Obesidade")
    else:
        print("Obesidade Grave")
        


    print(f"{calculo:.2f}")

imc()