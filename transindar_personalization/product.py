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
    quantity_per_pack = fields.Char(String='Cantidad por Pack')
    stk_tmp_ros = fields.Char('S. Rosario')
    stk_tmp_sfe = fields.Char('S. Santa Fe')
    stk_tmp_raf = fields.Char('S. Rafaela')

    @api.model
    def name_search(
            self, name, args=None, operator='ilike', limit=100):
        recs = self.search(self._get_search_domain(
            name, args=args, operator=operator, limit=limit), limit=limit)
        return recs.name_get()

    @api.model
    def _get_search_domain(
            self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            # if we found exact internal_code we return it
            if self.search(
                    [('internal_code', '=ilike', name)], limit=limit):
                return [('internal_code', '=ilike', name)]

            # if we found exact default_code we return it
            elif self.search(
                    [('default_code', '=ilike', name)], limit=limit):
                return [('default_code', '=ilike', name)]

            # else we return custom search
            else:
                return [
                    '|', '|', ('name', 'ilike', name),
                    ('product_brand_id.name', 'ilike', name),
                    ('supplier_code', 'ilike', name)]
        return args

    @api.model
    def _search_custom_search(self, operator, value):
        recs = self._get_search_domain(value, operator=operator)
        return recs

    @api.multi
    def _get_custom_search(self):
        return False

    custom_search = fields.Char(
        compute='_get_custom_search',
        string='Busqueda Inteligente',
        search='_search_custom_search'
    )


class ProductProduct(models.Model):
    _inherit = 'product.product'

    supplier_code = fields.Char(
        related='seller_ids.product_code', string="Supplier Code")
    location_1 = fields.Char(
        related='product_tmpl_id.location_1', String='Location 1')
    location_2 = fields.Char(
        related='product_tmpl_id.location_2', String='Location 2')

    @api.model
    def name_search(
            self, name, args=None, operator='ilike', limit=100):
        recs = self.search(self._get_search_domain(
            name, args=args, operator=operator, limit=limit), limit=limit)
        return recs.name_get()

    @api.model
    def _get_search_domain(
            self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            # if we found exact internal_code we return it
            if self.search(
                    [('internal_code', '=ilike', name)], limit=limit):
                return [('internal_code', '=ilike', name)]

            # if we found exact default_code we return it
            elif self.search(
                    [('default_code', '=ilike', name)], limit=limit):
                return [('default_code', '=ilike', name)]

            # else we return custom search
            else:
                return [
                    '|', '|', ('name', 'ilike', name),
                    ('product_brand_id.name', 'ilike', name),
                    ('supplier_code', 'ilike', name)]
        return args

    @api.model
    def _search_custom_search(self, operator, value):
        recs = self._get_search_domain(value, operator=operator)
        return recs

    @api.multi
    def _get_custom_search(self):
        return False

    custom_search = fields.Char(
        compute='_get_custom_search',
        string='Busqueda Inteligente',
        search='_search_custom_search'
    )


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
