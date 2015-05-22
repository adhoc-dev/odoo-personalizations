# -*- coding: utf-8 -*-
from openerp import fields, models


class res_partner(models.Model):
    _inherit = 'res.partner'

    user_id = fields.Many2one(
        default=False,
        )
