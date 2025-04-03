# Instrução 1: Executar LOAD M(100) (Carregar o valor 3 no AC)
# Ciclo de busca
# 1. MAR ← PC: O endereço da instrução é carregado no MAR.
# 2. MBR ← M(MAR): A instrução LOAD M(100) é carregada no MBR.
# 3. IR ← MBR(20:27): A instrução é armazenada no IR.
# 4. MAR ← MBR(28:39): O endereço 100 é carregado no MAR.
# 5. PC ← PC + 1: O PC avança para 1.
# Ciclo de execução
# 6. MBR ← M(MAR): O valor 3 é carregado no MBR.
# 7. AC ← MBR: O valor 3 é carregado no AC.

# Instrução 2: Executar ADD M(101) (Somar o valor 4 ao AC)
# Ciclo de busca
# 1. MAR ← PC: O endereço da instrução é carregado no MAR.
# 2. MBR ← M(MAR): A instrução ADD M(101) é carregada no MBR.
# 3. IR ← MBR(20:27): A instrução é armazenada no IR.
# 4. MAR ← MBR(28:39): O endereço 101 é carregado no MAR.
# 5. PC ← PC + 1: O PC avança para 2.
# Ciclo de execução
# 6. MBR ← M(MAR): O valor 4 é carregado no MBR.
# 7. AC ← AC + MBR: O valor 4 é somado ao AC (3 + 4 = 7).

# Ciclo de busca
# 1. MAR ← PC: O endereço da instrução é carregado no MAR.
# 2. MBR ← M(MAR): A instrução STOR M(102) é carregada no MBR.
# 3. IR ← MBR(20:27): A instrução é armazenada no IR.
# 4. MAR ← MBR(28:39): O endereço 102 é carregado no MAR.
# 5. PC ← PC + 1: O PC avança para 3.
# Ciclo de execução
# 6. MBR ← AC: O valor 7 (do AC) é carregado no MBR.
# 7. M(MAR) ← MBR: O valor 7 é armazenado na posição 102 da memória.

# Passo 4: Executar HALT (Finalizar a execução)
# Ciclo de busca
# 1. MAR ← PC: O endereço da instrução é carregado no MAR.
# 2. MBR ← M(MAR): A instrução HALT é carregada no MBR.
# 3. IR ← MBR(20:27): A instrução é armazenada no IR.
# 4. MAR ← MBR(28:39): “lixo” é carregado no MAR.
# 5. PC ← PC + 1: O PC avança para 4.
# Ciclo de execução
# 6. Execução interrompida: O programa para.

def ias():
    #INSTRUÇÕES
    halt = print("programa finalizado")
    v102 = []
    v101 = 4
    v100 = 3

    v1 = {"20:27": "STOR", "28:39": "M(102)", "0:8": "HALT"}
    v0 = {"20:27": "LOAD", "28:39": "M(100)", "0:8": "ADD", "9:19": "M(101)"}
    ac = [] 
    pc = v0
    
    #EXECUÇÃO
    ibr = []
    mar = pc
    print(f"Mar recebeu o valor que está no primeiro endereço que é agora é {mar}")
    mbr = v0
    print(f"Mbr recebeu oque está armazenado em mar {mar}")
    ir = mbr
    mar = mbr
    print(f"IR agora é {ir["20:27"]}\nmar agora é {"M(100)"}")
    mar = v100
    pc = v0
    print(f"PC agora é 1")
    mbr = mar
    print(f"MBR recebeu MAR que agora é {mar}")
    ac = mar
    print(f"AC recebe o valor de MAR que agora é {ac} ")
    mar = pc
    #novo ciclo
    pc = 2
    print(f"Mar recebeu o valor de {mar}")
    mbr = mar
    print(f"MBR recebe o valor de Mar que agora é {mbr}")
    ir = mbr['0:8']
    print(f"IR recebeu a instrução {ir}")
    mar = mbr['9:19']
    print(f"MAR recebeu {v101}")
    pc += 1
    print(f"PC agora é {pc}")
    ac += v101
    print(f"AC somou com ele mesmo {3} + o valor em MAR com {v101}" )
    v102 = ac
    print(f"M(102) recebeu o valor de AC :{v102},  ")
    pc += 1
    print(f"PC agora é {pc}")

ias()
