# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, fields


class res_company(models.Model):
    _inherit = 'res.company'

    preparation_time = fields.Integer(
        string='Preparation Time'
    )
