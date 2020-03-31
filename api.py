'''Api.py'''

import requests


base_url = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(idul):
    ''' Lister les parties.'''
    reponse = requests.get(base_url+'lister/', params={'idul': idul})
    if reponse.status_code == 200:
        reponse = reponse.json()
        return list(map(lambda x : x['id'], reponse['parties']))
    raise RuntimeError(reponse['message'])

def initialiser_partie(idul):
    '''Initialiser la partie'''
    rep = requests.post(base_url +'initialiser/', data={'idul': idul})
    rep = rep.json()
    msg = 'message'
    if (msg in rep.keys()):
        raise RuntimeError(rep['message'])
    return rep['id'], rep['état']

def jouer_coup(id, type, pos):
    '''Jouer un coup'''
    reponse = requests.post(base_url +'jouer/', data={'id':id, 'type':type, 'pos':pos})
    reponse = reponse.json()
    msg = 'message'
    win = 'gagnant'
    if (msg in reponse.keys()):
        raise RuntimeError(reponse['message'])
    elif (win in reponse.keys()):
        raise StopIteration(reponse["gagnant"])
    return reponse['état']
