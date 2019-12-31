# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Form request',
    'version' : '1.0',
    'summary': '',
    'sequence': 1,
    'description': """

    """,
    'category': 'Accounting',
    'website': 'https://www.odoo.com/page/billing',
    'depends' : [
        'base'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',

        'data/ir_sequence_data.xml',

        'views/form_request_view.xml',
        'views/product_request_view.xml',
        'views/system_request_view.xml',
    ],
    'author': 'Nguyen Quang Trong',
    'installable': True,
    'application': True,
    'auto_install': False,
}