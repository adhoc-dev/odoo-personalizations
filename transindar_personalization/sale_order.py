# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, api


class sale_order_line(models.Model):

    _inherit = 'sale.order.line'

    supplier_code = fields.Char(
        related='product_id.product_tmpl_id.supplier_code',
        readonly=True)
    internal_code = fields.Char(
        related='product_id.internal_code',
        readonly=True)
    product_brand_id = fields.Many2one(
        related='product_id.product_tmpl_id.product_brand_id',
        readonly=True)
    additional_description = fields.Char(
    )

    @api.one
    @api.onchange('additional_description')
    def change_additional_description(self):
        vals = self.product_id_change(
            pricelist=self.order_id.pricelist_id.id,
            product=self.product_id.id,
            partner_id=self.order_id.partner_id.id)
        name = vals.get('value', {}).get('name', False)
        if name:
            if self.additional_description:
                name = "%s\n%s" % (name, self.additional_description or '')
            self.name = name
