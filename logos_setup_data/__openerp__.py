# -*- coding: utf-8 -*-
{
    'name': 'Logos Set Up Data',
    'version': '8.0.1.0.0',
    'category': 'Accounting',
    'sequence': 14,
    'summary': '',
    'description': """
Logos Set Up Data & customizations
==================================
* make user (commercial) required on partners if "customer" is true
* no default user on partners
* setea los campos a mostrar en la vista tree de partner
* hacemos el campo user_id en invoices editable en cualquier momento
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'crm',
        'purchase',
        'sale',
        'portal_sale_distributor',
        'website_sale',
        'base_location',
        'price_security',
        'account_voucher_receipt',
        'product_price_currency',
        'logos_product_attributes',
        'product_catalog_aeroo_report',
    ],
    'data': [
        # Para arreglar error
        'security/ir.model.access.csv',
        'security/logos_security.xml',
        'report_data.xml',
        'product_view.xml',
        'receipt_view.xml',
        'crm_view.xml',
        'partner_view.xml',
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
