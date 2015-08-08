# -*- coding: utf-8 -*-
from openerp import models, fields


AVAILABLE_PRIORITIES = [
    ('1', 'Highest'),
    ('2', 'High'),
    ('3', 'Normal'),
    ('4', 'Low'),
    ('5', 'Lowest'),
]
# AVAILABLE_PRIORITIES = [
#     ('0', 'Low'),
#     ('1', 'Normal'),
#     ('2', 'High'),
#     ]
# AVAILABLE_PRIORITIES = [
#     ('-1', 'Lowest'),
#     ('0', 'fondo fa A.jpgLow'),
#     ('1', 'Normal'),
#     ('2', 'High'),
#     ('3', 'Highest'),
#     ]


class project_issue(models.Model):
    _inherit = "project.issue"

    priority = fields.Selection(
        AVAILABLE_PRIORITIES
        )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
