# -*- coding: utf-8 -*-
from openerp import fields, models


class product_template(models.Model):
    _inherit = 'product.template'

    sale_price_on_list_price_type_currency = fields.Float(
        string="Precio de venta (ARS)"
        )
