# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'inscription',
    'version': '13.0.1.0.0',
    'category': 'uncategorized',
    'author': 'hamza',
    'sequence': -100,
    'description': """
                this module allowed you to manage inscription in your system.
                   """,
    'summary': 'Inscription system',
    'website': 'https://www.odoo.com/app/inscription',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/management_view.xml',
        'report/inscription.xml',
        'report/report.xml',
    ],

    'demo': ['demo/demo.xml'],
    'image': [],
    'installable': True,
    'auto_install': False,
    #  'application': True,

    'license': 'LGPL-3',
}
