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
    'name': 'Estudios Integrales Customizations',
    'version': '8.0.1.0.0',
    'category': '',
    'sequence': 14,
    'summary': '',
    'description': """
Estudios Integrales Customizations
==================================
Modifications for Estudios Integrales
* Modificaciones en permisos relativos a multicompania
* Agregado control a document.directory a employees para que puedan borrar adjuntos
    """,
    'author':  'Sistemas ADHOC',
    'website': 'www.sistemasadhoc.com.ar',
    'images': [
    ],
    'depends': [
        'sale',
        'account',
        'hr_expense', 
        'project', 
        'document',
    ],
    'data': [
        'security.xml',
        'ir.model.access.csv',
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