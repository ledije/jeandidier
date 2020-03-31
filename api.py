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

