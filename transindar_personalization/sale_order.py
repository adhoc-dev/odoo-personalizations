# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, api
from datetime import datetime, timedelta


class sale_order(models.Model):

    _inherit = 'sale.order'

    sale_preparetion_time = fields.Integer(
        compute='_get_preparation_time',
        string='Tiempo De Preparacion')

    @api.one
    def _get_preparation_time(self):
        if self.company_id.preparation_time:
            preparation_time = self.company_id.preparation_time
            self.sale_preparetion_time = len(
                self.order_line) * preparation_time

    @api.one
    def update_requested_date(self):
        if self.sale_preparetion_time:
            self.requested_date = datetime.today() + timedelta(
                minutes=self.sale_preparetion_time)


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
