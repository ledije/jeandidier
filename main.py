''' Main.py  '''

import argparse
from api import lister_parties , jouer_coup, initialiser_partie


def analyser_commande():
    """Parser les valeurs """
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', help=' IDUL du joueur.')
    parser.add_argument('-l', '--lister', help='Lister les identifiants de vos 20 dernières parties.',
                        action='store_true')
    return parser.parse_args()

def afficher_damier_ascii(dictio):
    """Affiche le damier"""
    Parser_info = analyser_commande()
    dictio["joueurs"][0]["nom"] = Parser_info.idul
    Parser_info = dictio["joueurs"][0]["nom"]
    affichage = ''
    affichage += f'Légende: 1={Parser_info}, 2=automate'+'\n'
    affichage += 3*" "+35*"-"+'\n'
    resultat = []
    index = 10
    for i in range(9):
        resultat.append(['.' if i%4 == 0 else " " for i in range(33)])
        resultat.append([" " for _ in range(35)])
    resultat.pop(-1)
    player = dictio["joueurs"][0]
    bot = dictio["joueurs"][1]
    horizontaux = dictio["murs"]["horizontaux"]
    verticaux = dictio["murs"]["verticaux"]
    resultat[17-2*player["pos"][1]+1][4*(player["pos"][0]-1)] = str(1)
    resultat[17-2*bot["pos"][1]+1][4*(bot["pos"][0]-1)] = str(2)
    for horizontal in horizontaux:
        resultat[17-2*horizontal[1]+2][4*(horizontal[0]-1):4*(horizontal[0]-1)+5+2] = 7*"-"
    for vertical in verticaux:
        j = 0
        for i in range(3):
            m = 1 if j == 1 else 0
            resultat[17-2*(vertical[1]+i)+1+j][4*(vertical[0]-2)+2+m] = chr(124)
            j += 1
    for i, j in enumerate(resultat, 1):
        if (i%2 != 0):
            index -= 1
            affichage += str(index)+" "+chr(124)+" "+''.join(j)+" "+chr(124)+'\n'
        else:
            affichage += 2*" "+chr(124)+''.join(j)+chr(124)+'\n'
    affichage += f'{"--"+ chr(124)+35*"-"}'+'\n'
    affichage += f'{2*" "+chr(124)+" "}'
    for i in range(1, 10):
        affichage += f'{str(i)+3*" "}'
    affichage += '\n'
    return affichage

