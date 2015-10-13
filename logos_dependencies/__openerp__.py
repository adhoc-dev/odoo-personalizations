# -*- coding: utf-8 -*-
{
    'name': 'Logos Proyect Dependencies',
    'version': '8.0.1.0.0',
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
        # Dependencias fuertes (se necesitan por los datos que tocamos)
        # 'purchase',
        # 'crm',
        # Dependencias del proyecto
        'crm',
        'account_accountant',
        'account_check',
        'account_followup',
        'l10n_ar_chart_generic',
        'account_cancel',
        'auth_oauth',
        'portal_fix',
        'l10n_ar_bank',
        'l10n_ar_states',
        'account_journal_security',
        'account_clean_cancelled_invoice_number',
        'multi_store',
        'product_price_currency',
        'product_unique',
        'report_extended',
        'stock',
        'delivery',
        'partner_social_fields',
        'purchase',
        'purchase_double_validation',
        'website_sale',
        'sales_to_sale_order',
        'sale_stock_availability',
        'portal_sale_distributor',
        'product_visible_discount',
        # 'partner_state',
        'partner_school',
        'partner_views_fields',
        'sale_dummy_confirmation',
    ],
    'data': [
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
