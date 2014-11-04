# -*- coding: utf-8 -*-
{
    'name': 'Logos Set Up Data',
    'version': '1.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'description': """
Logos Set Up Data
=====================
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'crm',
        'purchase',
        'sale',
        'website_sale',
    ],
    'data': [
        # Para arreglar error
        'security/ir.model.access.csv',
        'security/logos_security.xml',
        'product_view.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: