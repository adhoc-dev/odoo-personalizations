# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, api
from openerp.osv import expression


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
    public_categ_2_ids = fields.Many2many(
        'product.public.category',
        string='Public Category2')
    public_categ_3_ids = fields.Many2many(
        'product.public.category',
        string='Public Category3')


class ProductProduct(models.Model):
    _inherit = 'product.product'

    supplier_code = fields.Char(
        related='seller_ids.product_code', string="Supplier Code")
    location_1 = fields.Char(
        related='product_tmpl_id.location_1', String='Location 1')
    location_2 = fields.Char(
        related='product_tmpl_id.location_2', String='Location 2')
    replanishment_discount_1 = fields.Float(
        related='product_tmpl_id.replanishment_discount_1',
        string='Replanishment Discount 1')
    replanishment_discount_2 = fields.Float(
        related='product_tmpl_id.replanishment_discount_2',
        string='Replanishment Discount 2')
    replanishment_discount_3 = fields.Float(
        related='product_tmpl_id.replanishment_discount_3',
        string='Replanishment Discount 3')
    replanishment_discount_4 = fields.Float(
        related='product_tmpl_id.replanishment_discount_4',
        string='Replanishment Discount 4')
    replanishment_surcharge_1 = fields.Float(
        related='product_tmpl_id.replanishment_surcharge_1',
        string='Replanishment Surcharge 1')
    replanishment_surcharge_2 = fields.Float(
        related='product_tmpl_id.replanishment_surcharge_2',
        string='Replanishment Surcharge 2')
    replanishment_surcharge_3 = fields.Float(
        related='product_tmpl_id.replanishment_surcharge_3',
        string='Replanishment Surcharge 3')
    replanishment_surcharge_4 = fields.Float(
        related='product_tmpl_id.replanishment_surcharge_4',
        string='Replanishment Surcharge 4')

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


class product_public_category(models.Model):
    _inherit = "product.public.category"

    def name_search(self, cr, uid, name, args=None, operator='ilike', context=None, limit=100):
        if not args:
            args = []
        if not context:
            context = {}
        if name:
            # Be sure name_search is symetric to name_get
            categories = name.split('/')
            parents = list(categories)
            child = parents.pop()
            domain = [('name', operator, child)]
            if parents:
                names_ids = self.name_search(
                    cr, uid, '/'.join(parents), args=args, operator='ilike', context=context, limit=limit)
                category_ids = [name_id[0] for name_id in names_ids]
                if operator in expression.NEGATIVE_TERM_OPERATORS:
                    category_ids = self.search(
                        cr, uid, [('id', 'not in', category_ids)])
                    domain = expression.OR(
                        [[('parent_id', 'in', category_ids)], domain])
                else:
                    domain = expression.AND(
                        [[('parent_id', 'in', category_ids)], domain])
                for i in range(1, len(categories)):
                    domain = [
                        [('name', operator, '/'.join(categories[-1 - i:]))], domain]
                    if operator in expression.NEGATIVE_TERM_OPERATORS:
                        domain = expression.AND(domain)
                    else:
                        domain = expression.OR(domain)
            ids = self.search(
                cr, uid, expression.AND([domain, args]), limit=limit, context=context)
        else:
            ids = self.search(cr, uid, args, limit=limit, context=context)
        return self.name_get(cr, uid, ids, context)

    def name_get(self, cr, uid, ids, context=None):
        res = []
        for cat in self.browse(cr, uid, ids, context=context):
            names = [cat.name]
            pcat = cat.parent_id
            while pcat:
                names.append(pcat.name)
                pcat = pcat.parent_id
            res.append((cat.id, '/'.join(reversed(names))))
        return res
