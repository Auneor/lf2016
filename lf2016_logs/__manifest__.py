# -*- coding: utf-8 -*-
{
    'name': "lf2016_logs",

    'summary': """
    Ce module gere les logs fortement signés afin de se mettre en conformité avec la loi finance 2016 (France)
        """,

    'description': """
    Ce module gere les logs fortement signés afin de se mettre en conformité avec la loi finance 2016 (France)
    """,

    'author': "Auneor Conseil",
    'website': "http://www.auneor-conseil.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
