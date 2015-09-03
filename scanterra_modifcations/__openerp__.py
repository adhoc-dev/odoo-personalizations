# -*- coding: utf-8 -*-
{
    'name': 'Scanterra Modifications',
    'version': '8.0.1.0.0',
    'category': 'Sales Management',
    'sequence': 14,
    'summary': 'Sales, Product, Category, Clasification',
    'description': """
Scanterra Modifications
=======================
* Restringir que las tareas creadas por un usuario, no las pueda eliminar otro usuario. Es decir que cada usuario solo pueda eliminar las tareas creadas por si mismo.
* Que se registre automáticamente como  una nota cuando se cambia alguna de los siguientes campos de la tarea (Resumen de la tarea (titulo), fecha limite, horas iniciales planificadas, fecha de inicio y fecha final) (actualmente solo registra en forma automática los cambios de estado).
* Ocultar el campo probabilidad en crm lead tree view

    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'depends': [
        'project',
        'project_issue',
        'l10n_ar_aeroo_sale',
        'crm',
    ],
    'data': [
        'security/project_security.xml',
        'crm_lead_view.xml',
        'phonecall_view.xml',
        'reports/sale_order_report.xml',
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
