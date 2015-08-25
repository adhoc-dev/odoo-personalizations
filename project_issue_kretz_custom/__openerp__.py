# -*- coding: utf-8 -*-
##############################################################################
#
#    Sistemas ADHOC - ADHOC SA
#    https://launchpad.net/~sistemas-adhoc
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
    'name': 'Project Issue Kretz Modifications',
    'version': '8.0.1.0.0',
    'category': 'Projects & Services',
    'sequence': 14,
    'summary': '',
    'description': """
Project Issue Kretz Modifications
=================================
    """,
    'author':  'Sistemas ADHOC',
    'website': 'www.sistemasadhoc.com.ar',
    'images': [
    ],
    'depends': [
        'project_issue_product',
        'project_issue_solutions',
        'disable_openerp_online',
        'project_issue_create_task_defaults',
    ],
    'data': [
        'project_issue_view.xml',
        'project_task_view.xml',
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
