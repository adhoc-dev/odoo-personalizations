# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class product_segment(osv.osv):
    _name = "product.segment"
    _description = "Product Segment"
    _order = "name"

    _constraints = [
        (osv.osv._check_recursion,
            'Error ! You cannot create recursive categories.', ['parent_id'])
    ]

    def name_get(self, cr, uid, ids, context=None):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        'name': fields.char(
            'Name', required=True, translate=True),
        'complete_name': fields.function(
            _name_get_fnc, type="char", string='Name'),
        'parent_id': fields.many2one(
            'product.segment', 'Parent Segment', select=True),
        'child_id': fields.one2many(
            'product.segment', 'parent_id', string='Children Segments'),
        'sequence': fields.integer(
            'Sequence',
            help="Gives the sequence order when displaying a list of product segments."),        
    }


class product_type(osv.osv):
    _name = "product.type"
    _description = "Type"
    _order = "name"

    _constraints = [
        (osv.osv._check_recursion,
            'Error ! You cannot create recursive categories.', ['parent_id'])
    ]

    def name_get(self, cr, uid, ids, context=None):
        if not len(ids):
            return []
        reads = self.read(cr, uid, ids, ['name', 'parent_id'], context=context)
        res = []
        for record in reads:
            name = record['name']
            if record['parent_id']:
                name = record['parent_id'][1]+' / '+name
            res.append((record['id'], name))
        return res

    def _name_get_fnc(self, cr, uid, ids, prop, unknow_none, context=None):
        res = self.name_get(cr, uid, ids, context=context)
        return dict(res)

    _columns = {
        'name': fields.char(
            'Name', required=True, translate=True),
        'complete_name': fields.function(
            _name_get_fnc, type="char", string='Name'),
        'parent_id': fields.many2one(
            'product.type', 'Parent Type', select=True),
        'child_id': fields.one2many(
            'product.type', 'parent_id', string='Children Type'),
        'sequence': fields.integer(
            'Sequence',
            help="Gives the sequence order when displaying a list of product Types."),
    }


class product_template(osv.osv):

    _inherit = 'product.template'

    _columns = {
        'type_id': fields.many2one('product.type', 'Type', ),
        'segment_id': fields.many2one('product.segment', 'Segment', ),
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
