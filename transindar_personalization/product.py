# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, api


class product_template(models.Model):

    _inherit = 'product.template'

    supplier_code = fields.Char(
        related='seller_ids.product_code', string="Supplier Code")
    location_1 = fields.Char(String='Location 1')
    location_2 = fields.Char(String='Location 2')
    replanishment_discount_1 = fields.Float('Replanishment Discount 1')
    replanishment_discount_2 = fields.Float('Replanishment Discount 2')
    replanishment_discount_3 = fields.Float('Replanishment Discount 3')
    replanishment_discount_4 = fields.Float('Replanishment Discount 4')
    replanishment_surcharge_1 = fields.Float('Replanishment Surcharge 1')
    replanishment_surcharge_2 = fields.Float('Replanishment Surcharge 2')
    replanishment_surcharge_3 = fields.Float('Replanishment Surcharge 3')
    replanishment_surcharge_4 = fields.Float('Replanishment Surcharge 4')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.one
    @api.depends(
        # because of being stored
        'product_tmpl_id.standard_price',
        'product_tmpl_id.replenishment_cost_currency_id',
        'product_tmpl_id.currency_replenishment_cost',
        'product_tmpl_id.replenishment_cost_currency_id.rate_ids.rate',
        'product_tmpl_id.replenishment_cost_currency_id.rate_ids.name',
        'product_tmpl_id.replanishment_discount_1',
        'product_tmpl_id.replanishment_discount_2',
        'product_tmpl_id.replanishment_discount_3',
        'product_tmpl_id.replanishment_discount_4',
        'product_tmpl_id.replanishment_surcharge_1',
        'product_tmpl_id.replanishment_surcharge_2',
        'product_tmpl_id.replanishment_surcharge_3',
        'product_tmpl_id.replanishment_surcharge_4'
    )
    def _get_replenishment_cost(self):
        # to_currency is price_type or user company currency
        to_currency = self.product_tmpl_id.get_currency_id()
        cost_currency = self.product_tmpl_id.replenishment_cost_currency_id
        currency_cost = self.product_tmpl_id.currency_replenishment_cost
        if cost_currency and currency_cost:
            if cost_currency != to_currency:
                replenishment_cost = cost_currency.compute(
                    currency_cost, to_currency)
            else:
                replenishment_cost = currency_cost
        else:
            replenishment_cost = self.standard_price
        discount_1 = self.product_tmpl_id.replanishment_discount_1
        discount_2 = self.product_tmpl_id.replanishment_discount_2
        discount_3 = self.product_tmpl_id.replanishment_discount_3
        discount_4 = self.product_tmpl_id.replanishment_discount_4
        surcharge_1 = self.product_tmpl_id.replanishment_surcharge_1
        surcharge_2 = self.product_tmpl_id.replanishment_surcharge_2
        surcharge_3 = self.product_tmpl_id.replanishment_surcharge_3
        surcharge_4 = self.product_tmpl_id.replanishment_surcharge_4
        self.replenishment_cost = replenishment_cost * (1 - discount_1 / 100) * (1 - discount_2 / 100) * (1 - discount_3 / 100) * (
            1 - discount_4 / 100) * (1 + surcharge_1 / 100) * (1 + surcharge_2 / 100) * (1 + surcharge_3 / 100) * (1 + surcharge_4 / 100)

    replenishment_cost = fields.Float(
        compute=_get_replenishment_cost)
