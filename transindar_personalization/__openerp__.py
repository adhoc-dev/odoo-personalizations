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
    'version': '8.0.0.1.1',
    'description': """
Transindar Personalization
==========================
    """,
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'depends': [
        'stock',
        'product_brand',
        'website_sale',
        'product_internal_code',
        'product_cost_currency',
        'product_price_currency',
<<<<<<< HEAD
        'partner_internal_code',
        'product_sale_price_by_margin',
        'sale_three_discounts',
        'sale_order_validity',
        'sale_procurement_date_confirm',
        'l10n_ar_invoice',
        'purchase_order_type',
        'sale_order_dates'
    ],
    'data': [
        'product_view.xml',
        'sale_order_view.xml'
    ],
=======
        'product_sale_price_by_margin',
        'sale_three_discounts',
        'sale_global_discount',
    ],
    'data': [
        'product_view.xml',
        'wizard/sale_global_discount_wizard_view.xml',
             ],
>>>>>>> d2ec9e3a6ac6aad2fadc8608eaf20e341b4700c5
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
