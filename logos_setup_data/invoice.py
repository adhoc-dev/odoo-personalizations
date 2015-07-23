# -*- coding: utf-8 -*-
from openerp import fields, models


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    user_id = fields.Many2one(
        readonly=False,
        )
