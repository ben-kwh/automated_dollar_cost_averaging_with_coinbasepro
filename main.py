# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:57:14 2019

@author: ben94
"""

import cbpro
import time

""" Paste your cbpro API keys into the below variables """
cbpro_apikey = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
cbpro_passphrase = 'your_passphrase'

""" Paste your bank account id into the funding_id variable.
Input the deposit amount that should be requested every time this function 
is run. The account id should be in quotes, the deposit amount should not. 
The deposit will initiate you run (or test) the function unless you set
the initiate_deposit_when_run variable to False.
Minimum coinbase deposit is $10.  Remember deposits on coinbase can take
10 days, so purchases may fail the first time this runs unless you already
have USD in your coinbase pro account. 
"""
initiate_deposit_when_run = True
funding_id = 'XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXXXXXXX'
deposit_amount = 10.00

"""Now tell the function which and how much of each crypto to buy.
Set True/False for each variable and set the amount of each to buy.
The default will buy $10 of bitcoin and nothing else."""
buys = {}
buys['BTC-USD'] = {'buy': True, 'amount': 10.00}
buys['ETH-USD'] = {'buy': False, 'amount': 0.00}
buys['LTC-USD'] = {'buy': False, 'amount': 0.00}

"""You can have the purchases you just made immediately withdrawn to your
own wallets. Set the True/False variable and input your wallet on the
address line.  """
withdraws = {}
withdraws['BTC-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['ETH-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}
withdraws['LTC-USD'] = {'withdraw': False,
                        'address': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'}

""" Don't modify anything under this line """
cbpro_api = cbpro.AuthenticatedClient(cbpro_apikey,
                                      cbpro_secret,
                                      cbpro_passphrase)


def automated_purchase(event, context):

    # Initiate a deposit ACH from your bank
    if initiate_deposit_when_run:
        dep_request = cbpro_api.deposit(amount=deposit_amount,
                                        currency='USD',
                                        payment_method_id=funding_id)
        print('dep_request: {}'.format(dep_request))
    # make purchases
    for key in buys.keys():
        if buys[key]['buy'] is True:
            order = cbpro_api.place_market_order(product_id=key,
                                                 side='buy',
                                                 funds=buys[key]['amount'])
            time.sleep(2)
            qty = float(cbpro_api.get_order(order['id'])['filled_size'])
            withdraws[key]['qty'] = qty

    # withdraw to wallets
    withdraws['BTC-USD']['base'] = 'BTC'
    withdraws['ETH-USD']['base'] = 'ETH'
    withdraws['LTC-USD']['base'] = 'LTD'

    for key in withdraws.keys():
        if withdraws[key]['withdraw'] is True:
            withdraw = cbpro_api.crypto_withdraw(amount=withdraws[key]['qty'],
                       currency=withdraws[key]['base'],
                       crypto_address=withdraws[key]['address'])
