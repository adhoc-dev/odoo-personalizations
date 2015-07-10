# -*- coding: utf-8 -*-
##############################################################################
#
#    Ingenieria ADHOC - ADHOC SA
#    https://launchpad.net/~ingenieria-adhoc
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

from openerp import netsvc
from openerp.osv import fields, osv, orm
from openerp.tools.translate import _

class sale_order_line(osv.osv):
    _inherit = "sale.order.line"

# Ahora no lo concatenamos porque lo agreagamos al reporte directamente, hacemos esto nuevo
    # def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
    #         uom=False, qty_uos=0, uos=False, name='', partner_id=False,
    #         lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
    #     res = super(sale_order_line, self).product_id_change(cr, uid, ids, pricelist, product, qty,
    #         uom, qty_uos, uos, name, partner_id,
    #         lang, update_tax, date_order, packaging, fiscal_position, flag, context)
    #     partner_obj = self.pool.get('res.partner')
    #     lang = partner_obj.browse(cr, uid, partner_id).lang
    #     context_partner = {'lang': lang, 'partner_id': partner_id}
    #     product_obj = self.pool.get('product.product')
    #     if product:
    #         product_obj = product_obj.browse(cr, uid, product, context=context_partner)        
    #         if not flag and product_obj.categ_id.name and res['value']['name']:
    #             res['value']['name'] = product_obj.categ_id.name + ' - '+ res['value']['name']
    #     return res

    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
            uom=False, qty_uos=0, uos=False, name='', partner_id=False,
            lang=False, update_tax=True, date_order=False, packaging=False, fiscal_position=False, flag=False, context=None):
        res = super(sale_order_line, self).product_id_change(cr, uid, ids, pricelist, product, qty,
            uom, qty_uos, uos, name, partner_id,
            lang, update_tax, date_order, packaging, fiscal_position, flag, context)
        partner_obj = self.pool.get('res.partner')
        lang = partner_obj.browse(cr, uid, partner_id).lang
        context_partner = {'lang': lang, 'partner_id': partner_id}
        product_obj = self.pool.get('product.product')
        attachment_obj = self.pool['ir.attachment']
        if product:
            if not flag:
                product_br = product_obj.browse(cr, uid, product, context=context_partner)        
                # Si hay desciprcion de venta, solo llevamos esta (sin nombre de producto)
                if product_br.description_sale:
                    res['value']['name'] = product_br.description_sale
                else:
                    res['value']['name'] = product_obj.name_get(cr, uid, [product_br.id], context=context_partner)[0][1]
                attachment_ids = attachment_obj.search(cr, uid, [('res_model','=','product.product'),('res_id','=',product)], context=context)
                if attachment_ids:
                    attachemnt_desc = ', '.join([at.name for at in attachment_obj.browse(cr, uid, attachment_ids, context=context)])
                    res['value']['name'] += '\n' + ('Ver adjuntos: ') + attachemnt_desc                                  
        return res    

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
