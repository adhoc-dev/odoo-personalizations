# -*- coding: utf-8 -*-
from openerp.osv import osv, fields


class account_invoice_report(osv.Model):
    _inherit = 'account.invoice.report'
    _columns = {
        'type_id': fields.many2one(
            'product.type', string='Product Type', readonly=True),
        'segment_id': fields.many2one(
            'product.segment', string='Product Segment', readonly=True),
    }

    def _select(self):
        return super(
            account_invoice_report, self)._select(
            ) + ", sub.type_id as type_id, sub.segment_id as segment_id"

    def _sub_select(self):
        return super(
            account_invoice_report, self)._sub_select(
            ) + ", pt.type_id as type_id, pt.segment_id as segment_id"

    def _group_by(self):
        return super(
            account_invoice_report, self)._group_by(
            ) + ", pt.type_id , pt.segment_id"
