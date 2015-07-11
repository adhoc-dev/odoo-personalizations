# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class sale_report(osv.osv):
    _inherit = "sale.report"

    _columns = {
        'type_id': fields.many2one(
            'product.type', string='Product Type', readonly=True),
        'segment_id': fields.many2one(
            'product.segment', string='Product Segment', readonly=True),
    }

    def _select(self):
        return super(
            sale_report, self)._select(
            ) + ", t.type_id as type_id, t.segment_id as segment_id"

    def _group_by(self):
        return super(
            sale_report, self)._group_by(
            ) + ", t.type_id , t.segment_id"

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
