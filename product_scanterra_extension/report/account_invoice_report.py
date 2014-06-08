# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (c) 2013 OpenERP S.A. <http://openerp.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp.osv import osv, fields

class account_invoice_report(osv.Model):
    _inherit = 'account.invoice.report'
    _columns = {
        'type_id': fields.many2one('product.type', string='Product Type', readonly=True, ),
        'segment_id': fields.many2one('product.segment', string='Product Segment', readonly=True, ),
    }

    def _select(self):
        return  super(account_invoice_report, self)._select() + ", sub.type_id as type_id, sub.segment_id as segment_id"

    def _sub_select(self):
        return  super(account_invoice_report, self)._sub_select() + ", pt.type_id as type_id, pt.segment_id as segment_id"

    def _group_by(self):
        return super(account_invoice_report, self)._group_by() + ", pt.type_id , pt.segment_id"
