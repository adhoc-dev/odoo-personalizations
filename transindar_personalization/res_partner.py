# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api, fields


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def name_search(
            self, name, args=None, operator='ilike', limit=100):
        recs = self.search(self._get_search_domain(
            name, args=args, operator=operator, limit=limit), limit=limit)
        if not recs:
            return super(res_partner, self).name_search(
                name=name, args=args, operator=operator, limit=limit)
        return recs.name_get()

    @api.model
    def _get_search_domain(self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []
        if name:
            if self.search(
                    [('internal_code', '=ilike', name)] + args,
                    limit=limit):
                return [('internal_code', '=ilike', name)] + args
            else:
                return ['|', '|', ('display_name', 'ilike', name),
                        ('ref', 'ilike', name), ('email', 'ilike', name)] + args
        return args

    def _search_custom_search(self, operator, value):
        res = self._get_search_domain(value, operator=operator)
        return res

    @api.multi
    def _get_custom_search(self):
        return False

    custom_search = fields.Char(
        compute='_get_custom_search',
        string='Busqueda Inteligente',
        search='_search_custom_search'
    )
