# -*- coding: utf-8 -*-
{
    'name': "Custom Receipt Module For POS ( Ahmeds )",

    'summary': """Custom Receipt Module For POS 
                Develope by ahmed salah
                you can contact me on Twitter @GeekAhmeds
                on github: GeekAhmeds
                visit my website https://www.ahmeds.me
                on FB: https://www.facebook.com/just.mewps
    """,

    'description': """
        New Module to fix receipt and get information for client such as name and number and address,
        you can add this for super market t delevery orders like a Home Delevery,
        and fix the orderlines for product and put in table to order the receipt,
        and get the number for order like Bill: 1, 2, 3 instead of order 0001-001-0001>
        Good Luck :).
    """,

    'author': "AhmedS",
    'website': "http://www.Ahmeds.me",
    "price": 9.5,
    "currency": "USD",
    'category': 'POS',
    'version': '0.1',

    # any module necessary for this one to work correctly
	'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'static/src/js/screen.js',
        
    ],
	'qweb': [
        'static/src/xml/receipt_client.xml',
        'static/src/xml/receipt_orderlines.xml',
        'static/src/xml/ordernumber.xml',
        ],
    # only loaded in demonstration mode
    'demo': [],
	'installable': True,
	'auto_install': False,
	'application': True,
}
