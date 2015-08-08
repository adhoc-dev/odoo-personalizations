# -*- coding: utf-8 -*-
from openerp import models, fields


AVAILABLE_PRIORITIES = [
    ('0', 'Very Low'),
    ('1', 'Low'),
    ('2', 'Normal'),
    ('3', 'High'),
    ('4', 'Very High'),
]


class crm_phonecall(models.Model):
    _inherit = "crm.phonecall"

    priority = fields.Selection(
        AVAILABLE_PRIORITIES
        )
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
