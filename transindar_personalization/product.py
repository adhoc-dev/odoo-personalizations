# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, _


class stock(models.Model):

    _inherit = 'product.template'

    supplier_code = fields.Char(
        related='seller_ids.product_code', string="Supplier Code")
    location_1 = fields.Char(String='Location 1')
    location_2 = fields.Char(String='Location 2')
