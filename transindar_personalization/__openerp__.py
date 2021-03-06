# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015  ADHOC SA  (http://www.adhoc.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'active': True,
    'name': 'Transindar Personalization',
    'category': 'Stock',
    'version': '8.0.0.26.0',
    'description': """
Transindar Personalization
==========================
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'sale_stock_availability',
        'product_brand',
        'product_website_categ_search',
        'product_internal_code',
        'stock_picking_list',
        'account_invoice_prices_update',
        'product_template_tree_prices',
        # 'product_price_currency',
        'partner_internal_code',
        # 'product_sale_price_by_margin',
        'sale_three_discounts',
        'sale_order_validity',
        # 'sale_procurement_date_confirm',
        # 'l10n_ar_invoice',
        # 'purchase_order_type',
        'sale_order_dates',
        'sale_global_discount',
        'l10n_ar_invoice',
        'sale_quotation_products',
        'account_invoice_control',
        'partner_no_auto_search',
        'product_no_auto_search',
        # 'web_sheet_full_width'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'product_view.xml',
        'sale_order_view.xml',
        'category_public_view.xml',
        'report_data.xml',
        'action_data.xml',
        'invoice_view.xml',
        'account_voucher_view.xml',
        'res_partner_view.xml',
        'stock_picking_view.xml',
        'res_company_view.xml'
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
