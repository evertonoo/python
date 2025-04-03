classes ={
    "Guerreiro": {
        "name": "Guerreiro",
        "desc": "Focado em combate corpo a corpo. Usa espadas de duas mãos. Alta resistência e defesa.",
        "hp": 90,
        "hp_max": 90,
        "mp": 30,
        "mp_max": 30,
        "Attck": 80,
        "AttckRate": 5,
        "Defense": 90,
        "Speed": 4,     
},    
    "Mago": {
        "name": "Mago",
        "desc": "Especialista em ataques mágicos. Usa orbes e veste túnicas leves. Baixa defesa, mas alto dano em área.",
        "hp": 50,
        "hp_max": 50,
        "mp": 100, 
        "mp_max": 100,
        "Attck": 70,
        "AttckRate": 6,
        "Defense": 30,
        "Speed": 5,
    },
    "Arqueiro":{
        "name": "Arqueiro",
        "desc": "Ataca à distância com cristal ou orb. Boa precisão e velocidade de ataque. Defesa Moderada",
        "hp": 60,
        "hp_max": 60,
        "mp": 40, 
        "mp_max": 40,
        "Attck": 70,
        "AttckRate": 9,
        "Defense": 50,
        "Speed": 8,
    },
    "Ladino":{
        "name": "Ladino",
        "desc": "Rápido e furtivo, usa adagas. Especialista em ataques críticos e evasão. Baixa resistência, mas alto dano por segundo.",
        "hp": 50,
        "hp_max": 50,
        "mp": 30, 
        "mp_max": 30,
        "Attck": 60,
        "AttckRate": 8,
        "Defense": 40,
        "Speed": 10,
    },
    "Paladino": {
        "name": "PaLadino",
        "desc": "Guerreiro sagrado, mistura ataque e defesa. Pode curar a si mesmo e aos aliados. Usa espadas e armaduras pesadas.",
        "hp": 80,
        "hp_max": 80,
        "mp": 60, 
        "mp_max": 60,
        "Attck": 70,
        "AttckRate": 5,
        "Defense": 80,
        "Speed": 3,
    }
}
itens = (
    #[Item] Type    PriceSell  Attck    AttckRate DefenRate MagAtt  MaxCore LimitLv LimitClass  LimitReputation Grade	
    (0, "1H_Sword", 10, 20, 80, 0, 0, 3, 0, 0, 1, 1),
    (1, "2H_Sword", 15, 40, 150, 0, 0, 3, 0, 0, 1, 1),
    (2, "Staff", 12, 10, 60, 0, 30, 3, 0, 0, 1, 1),
    (3, "Bow", 14, 25, 90, 0, 0, 3, 0, 0, 1, 1),
    (4, "Dagger", 11, 15, 110, 0, 0, 3, 0, 0, 1, 1),
    # Grade 2 - Raro
    (5, "1H_Sword", 50, 35, 90, 5, 0, 4, 0, 0, 2, 2),
    (6, "2H_Sword", 70, 70, 170, 5, 0, 4, 0, 0, 2, 2),
    (7, "ORB", 60, 20, 70, 0, 50, 4, 0, 0, 2, 2),
    (8, "CRYSTAL", 65, 40, 100, 5, 0, 4, 0, 0, 2, 2),
    (9, "Dagger", 55, 30, 120, 5, 0, 4, 0, 0, 2, 2),
    # Grade 3 - Épico
    (10, "1H_Sword", 200, 50, 100, 10, 0, 5, 0, 0, 3, 3),
    (11, "2H_Sword", 250, 90, 190, 10, 0, 5, 0, 0, 3, 3),
    (12, "Staff", 220, 30, 80, 0, 80, 5, 0, 0, 3, 3),
    (13, "Bow", 230, 55, 110, 10, 0, 5, 0, 0, 3, 3),
    (14, "Dagger", 210, 45, 130, 10, 0, 5, 0, 0, 3, 3),
    # Grade 4 - Lendário
    (15, "1H_Sword", 500, 70, 120, 15, 0, 6, 0, 0, 4, 4),
    (16, "2H_Sword", 600, 120, 210, 15, 0, 6, 0, 0, 4, 4),
    (17, "Staff", 550, 45, 90, 0, 120, 6, 0, 0, 4, 4),
    (18, "Bow", 580, 75, 130, 15, 0, 6, 0, 0, 4, 4),
    (19, "Dagger", 520, 65, 140, 15, 0, 6, 0, 0, 4, 4),
    # Grade 5 - Mítico
    (20, "1H_Sword", 1000, 100, 140, 20, 0, 7, 0, 0, 5, 5),
    (21, "2H_Sword", 1200, 150, 230, 20, 0, 7, 0, 0, 5, 5),
    (22, "Staff", 1100, 60, 100, 0, 160, 7, 0, 0, 5, 5),
    (23, "Bow", 1150, 95, 150, 20, 0, 7, 0, 0, 5, 5),
    (24, "Dagger", 1050, 85, 160, 20, 0, 7, 0, 0, 5, 5),
    
)
skills = {
    "001": {  # Guerreiro
        "Name": "Golpe Brutal",
        "Attack": 120,
        "AttckRate": 6,
        "MagAtt": 0,
        "CastingTime": 0.5,
        "LimitLv": 5,
        "LimitClass": "Guerreiro",
        "Grade": None
    },
    "002": {  # Guerreiro
        "Name": "Espada Vorpal",
        "Attack": 180,
        "AttckRate": 5,
        "MagAtt": 0,
        "CastingTime": 1.0,
        "LimitLv": 10,
        "LimitClass": "Guerreiro",
        "Grade": None
    },
    "003": {  # Mago
        "Name": "Bola de Fogo",
        "Attack": 0,
        "AttckRate": 4,
        "MagAtt": 150,
        "CastingTime": 1.2,
        "LimitLv": 5,
        "LimitClass": "Mago",
        "Grade": None
    },
    "004": {  # Mago
        "Name": "Tempestade Arcana",
        "Attack": 0,
        "AttckRate": 5,
        "MagAtt": 200,
        "CastingTime": 2.5,
        "LimitLv": 10,
        "LimitClass": "Mago",
        "Grade": None
    },
    "005": {  # Arqueiro
        "Name": "Flecha Perfurante",
        "Attack": 110,
        "AttckRate": 9,
        "MagAtt": 0,
        "CastingTime": 0.3,
        "LimitLv": 5,
        "LimitClass": "Arqueiro",
        "Grade": None
    },
    "006": {  # Arqueiro
        "Name": "Disparo Fantasma",
        "Attack": 140,
        "AttckRate": 10,
        "MagAtt": 0,
        "CastingTime": 0.7,
        "LimitLv": 10,
        "LimitClass": "Arqueiro",
        "Grade": None
    },
    "007": {  # Ladrão
        "Name": "Corte Sombrio",
        "Attack": 100,
        "AttckRate": 10,
        "MagAtt": 0,
        "CastingTime": 0.2,
        "LimitLv": 5,
        "LimitClass": "Ladrão",
        "Grade": None
    },
    "008": {  # Ladrão
        "Name": "Dança das Lâminas",
        "Attack": 130,
        "AttckRate": 12,
        "MagAtt": 0,
        "CastingTime": 0.5,
        "LimitLv": 10,
        "LimitClass": "Ladrão",
        "Grade": None
    },
    "009": {  # Paladino
        "Name": "Golpe Sagrado",
        "Attack": 90,
        "AttckRate": 5,
        "MagAtt": 50,
        "CastingTime": 0.8,
        "LimitLv": 5,
        "LimitClass": "Paladino",
        "Grade": None
    },
    "010": {  # Paladino
        "Name": "Luz Divina",
        "Attack": 120,
        "AttckRate": 6,
        "MagAtt": 70,
        "CastingTime": 1.5,
        "LimitLv": 10,
        "LimitClass": "Paladino",
        "Grade": None
    }
}
