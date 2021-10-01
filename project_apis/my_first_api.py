#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 10:41:57 2021

@author: alina

Resources: https://towardsdatascience.com/quick-fire-guide-to-apis-in-python-891dd98c8877
"""

import requests
import json

import apis_tokens

# get Charizard's abilities using GET

response = requests.get('https://pokeapi.co/api/v2/pokemon/charizard')
response

response.json()

for ability in response.json()['abilities']:
    print(ability['ability']['name'])


#######################################################
# using the GitHub API - create repo using POST

token = apis_tokens.apisToken

payload = {
    'name': 'api_test',
    'public': 'true'
}

res = requests.post('https://api.github.com/user/repos',
                    headers={'Authorization': f'token {token}'},
                    data=json.dumps(payload))
res





















