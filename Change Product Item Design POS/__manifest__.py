# -*- coding: utf-8 -*-
{
    'name': "Change Product Item Design",

    'summary': """
        Change Product Item Design For POS
        """,

    'description': """
        POS Change Product Item Design v15.0
Change Product Item Design make Your Product Item Without Image For Product, 
Large Name without image.
        POS,
        POS Shop,
        Point of Sales,
    """,

    'author': "Th3Company",
    'website': "http://th3company.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'currency': 'USD',
    'price': '0.0',
    'category': 'Point Of Sale',
    'support': 'info@th3company.com',
    'version': '15.0.0.1',
    'images': ['static/description/Untitled-1.png'],
    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],
    'assets': {
        'web.assets_qweb': [
           "receipt_pos/static/src/xml/th3C_Product_Item.xml",
        ],
        "point_of_sale.assets": [
            "receipt_pos/static/src/css/style.css",
        ],
    },
    # only loaded in demonstration mode

    'installable': True,
}
