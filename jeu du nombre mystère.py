import random

nombre_essai =5


x = random.randint(1,100)
print("🔥 Le jeu du nombre mystère 🔥\nDevine le nombre entre 1 et 100 \n\nIl te reste 5 essais")
while True : 
    MENU=f""" Devine le nombre :"""
    
    continuer=input(MENU) 
    if not continuer.isdigit():
        print('Veuillez entrer un nombre valide !\n')
        continue

    if int(continuer)==x :
        print(f"bravo tu a trouvé le nombre mystère qui été {x} MAIS QUEL BG")
        break
    elif int(continuer)!=x and int(continuer) > x:
        print(f"""\n\nLe nombre mystère est plus petit que {continuer} \n\nIl te reste {nombre_essai-1} essais""")
    elif int(continuer)!=x and int(continuer)<x : 
        print(f"""\n\nLe nombre mystère est plus grand que {continuer} \n\nIl te reste {nombre_essai-1} essais""")
    nombre_essai -= 1 

    if nombre_essai==0 : 
        print(f"""😢 "snif" t'as perdu ! Le nombre mystère était {x}""")
        break
    