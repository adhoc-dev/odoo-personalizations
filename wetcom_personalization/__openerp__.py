# -*- coding: utf-8 -*-
{
    'active': True,
    'name': 'Wetcom Personalization',
    'category': 'Account',
    'version': '8.0.1.0.0',
    'description': """
    Wetcom Personalization
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar/',
    'license': 'AGPL-3',
    'depends': [
        'sale', 'crm', 'delivery', 'account_analytic_analysis', 'purchase',
        'help_doc_crm', 'sale_commission'
    ],
    'data': [
        'security/wetcom_group.xml',
        # 'security/wetcom_security.xml',
        'security/ir.model.access.csv',
        'wetcom_workflow.xml',
        'sale_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
