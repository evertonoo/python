import geral

    #Mostra as classes disponiveis, para escolha
def escolhe_classe():
    n = 0
    print("Classes Disponíveis")
    for c in geral.classes:
        n += 1
        print(f"{n} - {c}")

    classe = int(input("Por favor digite á classe que escolheu: "))
    while classe < 1 or classe > 5:
        classe = int(input("Classe não existe por favor digite um numero de 1 a 5: \r"))
    
    if classe == 1:
       classe = geral.classes["Guerreiro"]
    elif classe == 2:
       classe = geral.classes["Mago"]
    elif classe == 3:
       classe = geral.classes["Arqueiro"]
    elif classe == 4:
       classe = geral.classes["Ladino"]
    else:
       classe = geral.classes["Paladino"]
    return classe

personagem = escolhe_classe()

print(f"\nEstá e á classe escolhida:\n\nClasse: {personagem['name']}\nHP: {personagem['hp']}/{personagem['hp_max']}\nMP: {personagem['mp']}/{personagem['mp_max']}\nAtaque: {personagem['Attck']}\nDefesa: {personagem['Defense']}\nDeseja continuar: S/N")
