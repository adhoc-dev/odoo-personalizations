# -*- coding: utf-8 -*-
{
    'name': 'Scanterra Modifications',
    'version': '1.0',
    'category': 'Sales Management',
    'sequence': 14,
    'summary': 'Sales, Product, Category, Clasification',
    'description': """
Scanterra Modifications
=======================
* Restringir que las tareas creadas por un usuario, no las pueda eliminar otro usuario. Es decir que cada usuario solo pueda eliminar las tareas creadas por si mismo.
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'depends': [
        'project',
    ],
    'data': [
        'security/project_security.xml',
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