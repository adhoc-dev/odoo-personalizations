# -*- coding: utf-8 -*-
from openerp import fields, models


class product_template(models.Model):
    _inherit = 'product.template'

    cia_currency_list_price = fields.Float(
        string="Precio de venta (ARS)"
        )
