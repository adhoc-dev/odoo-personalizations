# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class stock(models.Model):

    _inherit = 'stock.transfer_details'

    scale_read = fields.Float(string="Scale Read")
