from math import *
from time import *
from colored import fg
from os import system
# Variables
r = fg('red')
g = fg('green')
ye = fg('yellow')
w = fg('white')
pp = fg('purple_4a')
go = fg('gold_3a')
bl = fg('blue')
lb = fg('light_blue') 
lr = fg('light_red')
ly = fg('light_yellow')
lg = fg('light_green')
bla = fg('black')
gray = fg('dark_gray')

clear = lambda: system('clear')
# Textes
banner = f"""    {pp} _    _                     ___             _   _             
    {go}| |  (_)_ _  ___ __ _ _ _  | __|  _ _ _  __| |_(_)___ _ _  ___
    {ye}| |__| | ' \/ -_) _` | '_| | _| || | ' \/ _|  _| / _ \ ' \(_-<
    {bl}|____|_|_||_\___\__,_|_|   |_| \_,_|_||_\__|\__|_\___/_||_/__/{w}
                                                               
"""
toprint = f"""
    Fait par {go}willyrire,{w}
    Version {bl}1.0.0{w}

    Nom du Projet: {pp}Fonctions Linéaires{w}
    Ce programme sert principalement à vous aidez à calculer la règle de la fonction linéaire que vous aurez \n    choisi.

    Comment ça marche?

    Lorsque le programme vous demandera de donner 2 coordonnées, il le demandera de cette façon, x1 y1 x2 y2, \n    pour que vous sachiez ce que signifient ces 4 choses, imaginez que vous avez 2 points, A(x,y) et \n    B(x,y) x1 est égal à A(x) et y1 est égal à A(y). x2 sera égal à B(x) et y2 sera égal à B(y). Vous \n    devez les donner dans le bon ordre pour obtenir le meilleur résultat. N'oubliez pas qu'une erreur \n    peut survenir.\n    Vous pouvez annuler toutes actions à n'importe quel moment, pour cela, dite {lr}cancel {w}dans n'importe quel champ.{w}"""
settprint = f"""
    Configurations Possible:

    1) Exponetielle         4) Quadratique
    2) Partielle            5) Direct
    3) Inverse              6) {lr}Quitter le Programme{w}
"""
goodbye = f"\n   {w}Aurevoir ! :)"
comeback = f"\n    {w}Tes souhaits ont été entendu !"
comparr = f"\n    {w}Veuillez remplir les champs suivants avec des nombres.\n    {ly}Lorsque le programme vous demandera de donner 2 coordonnées, il le demandera de cette façon, x1 y1 x2 y2, \n    pour que vous sachiez ce que signifient ces 4 choses, imaginez que vous avez 2 points, A(x,y) et \n    B(x,y) x1 est égal à A(x) et y1 est égal à A(y). x2 sera égal à B(x) et y2 sera égal à B(y). Vous \n    devez les donner dans le bon ordre pour obtenir le meilleur résultat. N'oubliez pas qu'une erreur \n    peut survenir.{w}"
cancelsucc = f"\n    {w}Opération cancellé avec {lg}succès{w} !"

#codes d'erreur

e404 = f"\n    {lr}Code d'erreur 404\n\n    {ly}La configuration demandé n'a pas pu être trouvé\n{w}"
e408 = f"\n    {lr}Code d'erreur 408\n\n    {ly}La syntaxe indiqué n'a pas pu être traité correctement.{w}"
e409 = f"\n    {lr}Code d'erreur 409\n\n    {ly}Les données demandé sont des chiffres et ne sont pas supposé de contenir des caractère alphabétique.\n    Que des nombres entier ou décimale."
edumb = f"\n    {lr}Code d'erreur DUMB\n\n    {ly}Mon niveau de connaissance ne me permet pas de trouver le facteur multiplicatif avec\n    les informations que vous m'avez fourni."
e304 = f"\n    {lr}Code d'erreur 304\n\n    {ly}Les coordonnées que vous avez fourni ne représente pas la fonctions sélectionnée{w}"

# Arrays
options = ("1", "2", "3", "4", "5", "6")
leaopt = ("y", "yes", "ye", "yeah", "confirm")
cleaopt = ("n", "no", "nah", "nope", "cancel", "na")
cop = ("cancel", "stop", "arrête", "fin", "cance", "sto")

def menu():
    clear()
    print(banner)
    print(toprint)
    print(settprint)
    cmd = input(f"    {lb}Veuillez Choisir une configuration: {w}")
    # Ont vérifie que l'utilisateur a pris une configuration valide
    clear()
    if cmd in options:
        if cmd == "6":
            conf = input(f"\n    Êtes-vous sûr de vouloir {lr}quitter {w}le programme? ({lr}Y{w}/{lg}N{w}): ")
            clear()
            if conf.lower() in leaopt:
                print(goodbye)
                sleep(3)
            elif conf.lower() in cleaopt:
                print(comeback)
                sleep(2)
                return menu()
            else:
                print(e408)
                sleep(2)
                return menu()
        # Exponentielle
        if cmd == "1":
            def expo():
                clear()
                print(comparr)
                x1 = input("\n    X1 : ")
                if x1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return expo()
                # 
                y1 = input("\n    Y1 : ")
                if y1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return expo()
                #
                x2 = input("\n    X2 : ")
                if x2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return expo()
                #
                y2 = input("\n    Y2 : ")
                if y2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return expo()
            
                # Now that they all passed the numeric check, we can put them as int here
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)

                A = f"A({x1},{y1})"
                B = f"B({x2},{y2})"

                if x1 == 0:
                    a = y1
                    # Variable pour le calcul f(x) = a(c)*x  | Ont remple le f(x) par y et le x par x
                    y = y2 # y2 = a(c)*x
                    x = x2
                    c1 = y/a
                    c = c1 ** (1/x)

                    # ont renvoie le résultat avec les calculs
                    clear()
                    result = f"""
    Fonctions : Exponentielle

    Coordonnées : {A} et {B}

    Calculs;

    1. Trouver le facteur multiplicatif

        #-> Puisque x1 = 0 nous savons déjà que le y1 est le facteur multiplicatif.
        f(x) = {a}(c)*x

    2. Trouver la base

        f(x) = {a}(c)*x | Ont remplace avec les coordonnées de {B}
        {y} = {a}(c)*{x}
        {y}/{a}  = ({a}(c)*{x})/{a}
        {y}  =  c*{x}
        {x}*√{y} = {x}*√c*{x}
        {c}  = c
    
    3. Résultat

        >>> f(x) = {a}({c})*x <<<
"""
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
                elif x2 == x1+1 or x2 == x1-1:
                    # fm
                    fm = y1/y2
                    a = y1 * fm ** x1
                    
                    # Trouver la base

                    y = y2 # y2 = a(c)*x
                    x = x2
                    c1 = y/a
                    c = c1 ** (1/x)

                    # ont renvoie le résultat avec les calculs
                    clear()
                    result = f"""
    Fonctions : Exponentielle

    Coordonnées : {A} et {B}

    Calculs;

    1. Trouver le facteur multiplicatif

        #-> Puisque x1 = 0 nous savons déjà que le y1 est le facteur multiplicatif.
        f(x) = {a}(c)*x

    2. Trouver la base

        f(x) = {a}(c)*x | Ont remplace avec les coordonnées de {B}
        {y} = {a}(c)*{x}
        {y}/{a}  = ({a}(c)*{x})/{a}
        {y}  =  c*{x}
        {x}*√{y} = {x}*√c*{x}
        {c}  = c
    
    3. Résultat

        >>> f(x) = {a}({c})*x <<<
"""
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
                else:
                    clear()
                    print(edumb)
                    sleep(5)
                    return menu()
            expo()
        # Partielle
        if cmd == "2" or cmd == "5":
            def partielle():
                clear()
                print(comparr)
                x1 = input("\n    X1 : ")
                if x1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return partielle()
                # 
                y1 = input("\n    Y1 : ")
                if y1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return partielle()
                #
                x2 = input("\n    X2 : ")
                if x2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return partielle()
                #
                y2 = input("\n    Y2 : ")
                if y2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return partielle()
            
                # Now that they all passed the numeric check, we can put them as int here
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)

                A = f"A({x1},{y1})"
                B = f"B({x2},{y2})"

                # y = ax + b | a = ∆y/∆x
                c1a = y2 - y1
                c2a = x2 - x1
                a = c1a/c2a

                #b:
                # y = ax+b
                c1b = a*x1
                if c1b > 0:
                    b = y1-c1b
                    result = f"""
    Fonction : Partielle
    
    Coordonnées : {A} {B}

    Calculs :

    1. y = ax + b
    
    a = ∆y / ∆x
    a = {y2} - {y1} / {x2} - {x1}
    a = {c1a} / {c2a}
    a = {a}

    y = {a}x

    2. Trouver B en utilisant {A}
    
    y = ax + b
    {y1} = {a}({x1}) + b
    {y1} = {c1b} + b
    -{c1b} = -{c1b}
    {b} = b

    Réponse:

        >>> y = {a}x + {b} <<< 

"""
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
                elif c1b < 0:
                    b = y1+c1b
                    result = f"""
    Fonction : Partielle
    
    Coordonnées : {A} {B}

    Calculs :

    1. y = ax + b
    
    a = ∆y / ∆x
    a = {y2} - {y1} / {x2} - {x1}
    a = {c1a} / {c2a}
    a = {a}

    y = {a}x

    2. Trouver B en utilisant {A}
    
    y = ax + b
    {y1} = {a}({x1}) + b
    {y1} = {c1b} + b
    +{c1b} = +{c1b}
    {b} = b

    Réponse:

        >>> y = {a}x + {b} <<< 

"""
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
                elif c1b == 0:
                    clear()
                    result = f"""
    Fonction : Directe
    
    Coordonnées : {A} {B}

    Calculs :

    1. y = ax
    
    a = ∆y / ∆x
    a = {y2} - {y1} / {x2} - {x1}
    a = {c1a} / {c2a}
    a = {a}

    y = {a}x

    Réponse:

        >>> y = {a}x <<< 

"""
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
            partielle()
        # Inverse
        if cmd == "3":
            def inverse():
                clear()
                print(comparr)
                x1 = input("\n    X1 : ")
                if x1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return inverse()
                # 
                y1 = input("\n    Y1 : ")
                if y1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return inverse()
                #
                x2 = input("\n    X2 : ")
                if x2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return inverse()
                #
                y2 = input("\n    Y2 : ")
                if y2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return inverse()
            
                # Now that they all passed the numeric check, we can put them as int here
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)

                A = f"A({x1},{y1})"
                B = f"B({x2},{y2})"

                # Ont vérifi que x*y est égale à la même chose sur les deux points
                ic1 = x1 * y1
                ic2 = x2 * y2
                if ic1 == ic2:
                    k = x1 * y1
                    result = f"""
    Fonction : Inverse

    Coordonnées : {A} {B}

    Règle: f(x) = K/x

    Calculs:

    1. Trouver le total
        Total = K
        K = x1 * y1
        K = {x1} * {y1}
        K = {k}
        {gray}#-> si x1 * y1 est égale à x2 * y2, la fonction est bien l{w}

    Résultat:

        >>> f(x) = {k}/x
"""                     
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
                else:
                    clear()
                    print(e304)
                    sleep(5)
                    clear()
                    return inverse()
            inverse()
        # Quadratique
        if cmd == "4":
            def quadratique():
                clear()
                print(comparr)
                x1 = input("\n    X1 : ")
                if x1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return quadratique()
                # 
                y1 = input("\n    Y1 : ")
                if y1.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y1.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return quadratique()
                #
                x2 = input("\n    X2 : ")
                if x2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif x2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return quadratique()
                #
                y2 = input("\n    Y2 : ")
                if y2.lower() in cop:
                    clear()
                    print(cancelsucc)
                    sleep(2)
                    return menu()
                elif y2.isnumeric() == False:
                    clear()
                    print(e409)
                    sleep(3)
                    clear()
                    return quadratique()
            
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)

                A = f"A({x1},{y1})"
                B = f"B({x2},{y2})"

                # Quadratique check

                qc1 = x1 ** x1
                qc2 = x2 ** x2
                qc3 = x1 * y2
                qc4 = x2 * y1

                if qc3 == qc4:
                    print("Good functions")

                    # f(x) = ax²
                    y = y1
                    x = x1
                    ac1 = x ** 2
                    a = y/ac1
                    clear()    
                    result = f"""
    Fonction : Quadratique

    Coordonnées : {A} {B}

    Calculs :

    1. Trouver a en utilisant {A}

    f(x) = ax²
    {y1} = a({x1})² {gray}#-> Ont fait x²{w}
    {y1} = {ac1}a
    {y1}/{ac1} = {ac1}/{ac1}
    {a} = a

    Résultat:

        >>> f(x) = {a}x²
"""         
                    clear()
                    print(result)
                    finished = input("\n Lorsque tu as fini, just clique sur ENTER")
                    if finished != True:
                        clear()
                        return menu()
                else:
                    clear()
                    print(e304)
                    sleep(5)
                    return quadratique()
            quadratique()
    else:
        clear()
        print(e404)    
        sleep(5)
        return menu()
menu()
