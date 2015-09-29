# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class sale_order_line(models.Model):

    _inherit = 'sale.order.line'

    supplier_code = fields.Char(
        related='product_id.product_tmpl_id.supplier_code')
    internal_code = fields.Char(
        related='product_id.internal_code')
    product_brand_id = fields.Many2one(
        related='product_id.product_tmpl_id.product_brand_id')
