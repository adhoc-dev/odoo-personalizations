# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api, fields


class res_partner(models.Model):
    _inherit = 'res.partner'

    def name_search(self, cr, uid, name, args=None,
                    operator='ilike', context=None, limit=100):
        args = args or []
        res = []
        if name:
            recs = self.search(
                cr, uid, [('internal_code', '=ilike', name)],
                limit=limit, context=context)
            if recs:
                res = self.name_get(cr, uid, recs)
            else:
                recs = self.search(
                    cr, uid, [('ref', 'ilike', name)] + args,
                    limit=limit, context=context)
                res = self.name_get(cr, uid, recs)
                res += super(res_partner, self).name_search(
                    cr, uid,
                    name=name, args=args, operator=operator, limit=limit)
        else:
            res = super(res_partner, self).name_search(
                    cr, uid,
                    name=name, args=args, operator=operator, limit=limit)
        return res

    def _search_custom_search(self, operator, value):
        res = self.name_search(value, operator=operator)
        return [('id', 'in', [x[0] for x in res])]

    @api.multi
    def _get_custom_search(self):
        return False

    custom_search = fields.Char(
        compute='_get_custom_search',
        string='Busqueda Inteligente',
        search='_search_custom_search'
        )
