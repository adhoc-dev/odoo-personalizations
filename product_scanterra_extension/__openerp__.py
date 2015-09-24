# -*- coding: utf-8 -*-
##############################################################################
#
#    Ingenieria ADHOC - ADHOC SA
#    https://launchpad.net/~ingenieria-adhoc
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
    'name': 'Product Scanterra Extension',
    'version': '8.0.1.1.0',
    'category': 'Sales Management',
    'sequence': 14,
    'summary': 'Sales, Product, Category, Clasification',
    'description': """
Product Scanterra Extension
===========================
Adds new clasification for products called "product communication block" and "product segment". 
It also adds those fields in sale and invoice reports.
    """,
    'author':  'ADHOC SA',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'product',
        # 'sale_stock',
        # 'sale_order_mail_product_attachment',
    ],
    'data': [
        'product_view.xml',
        'report/sale_report_view.xml',
        'report/account_invoice_report_view.xml',
        'security/ir.model.access.csv',
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