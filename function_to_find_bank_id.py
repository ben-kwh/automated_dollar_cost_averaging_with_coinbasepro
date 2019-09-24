# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:33:37 2019

@author: ben94

This function is used only to determine the coinbase unique id number 
for your bank account.

From the Create Function screen in Google Cloud Console - Cloud Functions
Name:  get_cbp_funding_sources
Memory allocated: 128 MB
Trigger: HTTP
Allow unauthenticated invocations: check
Source Code: Inline editor
Runtime: Python 3.xx
Function to execute: print_cbpro_funding_accounts

Delete all the example code in the main.py and requirements.txt window

requirements.txt should be one word: cbpro

"""

# past the next 14 lines into the main.py window
import cbpro

""" paste your coinbase api info into into the variables below within
the quote marks. """
cbpro_apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_passphrase = 'your_passphrase'


def print_cbpro_funding_accounts(requests):

    cbpro_api = cbpro.AuthenticatedClient(cbpro_apikey,
                                          cbpro_secret,
                                          cbpro_passphrase)

    for funding_account in cbpro_api.get_payment_methods():
        print('the id number for {} is: {}'.format(funding_account['name'],
              funding_account['id']))
