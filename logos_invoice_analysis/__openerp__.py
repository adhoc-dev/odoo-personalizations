# -*- coding: utf-8 -*-
{
    'active': True,
    'name': 'Logos Invoice Analysis',
    'category': 'Account',
    'version': '8.0.1.0.0',
    'description': """
    This module provides Invoice Analysis for Logos implmentation
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'account',
        'l10n_ar_invoice',
        'product_bookstore',
        'logos_product_attributes',
        ],
    'data': [
        'security/ir.model.access.csv',
        'report/logos_invoice_analysis.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
