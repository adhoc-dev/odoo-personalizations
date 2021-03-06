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
    'name': 'Salve Regina Picking Report',
    'version': '8.0.0.0.0',
    'author': 'ADHOC SA',
    'license': 'AGPL-3',
    'category': 'base.module_category_knowledge_management',
    'website': 'www.adhoc.com.ar',
    'description': """
Salve Regina Picking Report
===========================
""",
    'test': [],
    'depends': [
        'l10n_ar_aeroo_base',
        'sale',
        'report_aeroo',
    ],
    'demo': [
    ],
    'data': [
        'report/stock_picking_report.xml',
    ],
    'installable': True,
}
