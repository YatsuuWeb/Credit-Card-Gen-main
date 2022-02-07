from random import Random
from pycenter import center
from os import terminal_size
from math import exp
import random, time





from pystyle import *
from os import system, name
import os

def clear():
    system("cls" if name == "nt" else clear)



if name == "nt":
    system("title Checker & mode 160 ,50")




banner = """\n   
                                                                                
                                                                                
                                                                                
                     ..,**,.                                                    
                  .*(#%%(*,.                                                    
              .,*(#&@&&#/.                                                      
            .*(%&@@@&#/*.                                                       
          .*/#&@@@@&%(,.                                                        
        .,/#&@@@@@@%(*,                                                         
       .*(%&@@@@@@@#/*.                                                         
      .*/%@@@@@@@@@%/*.                                                         
      *(%&@@@@@@@@@#/*.                                                         
    .,/#&@@@@@@@@@@%(*.                                                         
    ,*(%&@@@@@@@@@@&%(,.                                                        
    ,*(%@@@@@@@@@@@@&%(*.                                                       
    ,*(%@@@@@@@@@@@@@&%(,                                                       
    ,*(%@@@@@@@@@@@@@@@&#*,                                           ....      
    .*(%&@@@@@@@@@@@@@@@&#(*,.                                      .,///*.     
     ./#&&@@@@@@@@@@@@@@@@&%#/,.                                 .*(#%%#*..     
      ,/#&@@@@@@@@@@@@@@@@@@@&%(/,.                           .,*(#&@&%(*.      
      .,/#@@@@@@@@@@@@@@@@@@@@@@@&#(/*,..              ...,*/(%&&@@@@%/*.       
        ,/%&@@@@@@@@@@@@@@@@@@@@@@@@@&&%#((//**,,,**//((#%%&@@@@@@@&%(*,        
         ,/#%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%(*.          
          .,/#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#/,.           
             .*(%&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&%#/,.             
               .*/#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#(*,.               
                  .,/(%&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&&%(/,.                   
                     .,*/(#%&@@@@@@@@@@@@@@@@@@@@@&%%#/*,.                      
                           ..,**//(#########(/**,,..                            
                                   ...    .                                     
                                                                                                        
"""    






Anime.Fade(Center.Center(banner), Colors.purple_to_blue, Colorate.Vertical,interval=0.002, enter=True)

banner1 ="""

▄█▄    ▄█▄            ▄   ▄█    ▄▄▄▄▄   ██   
█▀ ▀▄  █▀ ▀▄           █  ██   █     ▀▄ █ █  
█   ▀  █   ▀      █     █ ██ ▄  ▀▀▀▀▄   █▄▄█ 
█▄  ▄▀ █▄  ▄▀      █    █ ▐█  ▀▄▄▄▄▀    █  █ 
▀███▀  ▀███▀        █  █   ▐               █ 
                     █▐                   █  
                     ▐                   ▀   

"""
System.Size(160, 30)
print(Colorate.Vertical(Colors.purple_to_blue, center(banner1, space=60), stop=20))





print("This generator only generates Visa credit cards.")
nb_nitros = int(input(Colorate.Vertical(Colors.purple_to_blue, "Veuillez saisir le nombre de cartes à générer: ")))
nb = 1
print("Génération de la carte de crédits..")
while nb <= nb_nitros:
    exp_date2 = str(random.randint(1, 12))
    if exp_date2 == str(1):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(2):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(3):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(4):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(5):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(6):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(7):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(8):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(9):
        exp_date2 = "0" + exp_date2
    elif exp_date2 == str(10):
        pass
    elif exp_date2 == str(11):
        pass
    elif exp_date2 == str(12):
        pass
    card = "4540 03" + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999)) + " | " + exp_date2 + "/"  + str(random.randint(21, 26)) + " | " + str(random.randint(100, 999))
    f = open('Codes.txt', "a+")
    f.write(f'{card}\n')
    f.close()

    print(f"[GENERATED] - {card}")
    time.sleep(0.025)
    nb += 1






"""
Ds:
> Kyото Web -$#6666
"""