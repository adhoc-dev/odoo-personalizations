# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models, api
from datetime import datetime


class stock(models.TransientModel):

    _inherit = 'stock.transfer_details'

    # se duplico por que no es facil modificarla
    @api.one
    def do_detailed_transfer(self):
        processed_ids = []
        # Create new and update existing pack operations
        for lstits in [self.item_ids, self.packop_ids]:
            for prod in lstits:
                pack_datas = {
                    'product_id': prod.product_id.id,
                    'product_uom_id': prod.product_uom_id.id,
                    'product_qty': prod.quantity,
                    'package_id': prod.package_id.id,
                    'lot_id': prod.lot_id.id,
                    'scale_in': prod.scale_in,
                    'scale_out': prod.scale_out,
                    'location_id': prod.sourceloc_id.id,
                    'location_dest_id': prod.destinationloc_id.id,
                    'result_package_id': prod.result_package_id.id,
                    'date': prod.date if prod.date else datetime.now(),
                    'owner_id': prod.owner_id.id,
                }
                if prod.packop_id:
                    prod.packop_id.with_context(
                        no_recompute=True).write(pack_datas)
                    processed_ids.append(prod.packop_id.id)
                else:
                    pack_datas['picking_id'] = self.picking_id.id
                    packop_id = self.env[
                        'stock.pack.operation'].create(pack_datas)
                    processed_ids.append(packop_id.id)
        # Delete the others
        packops = self.env['stock.pack.operation'].search(
            ['&', ('picking_id', '=', self.picking_id.id), '!',
                ('id', 'in', processed_ids)])
        packops.unlink()

        # Execute the transfer of the picking
        self.picking_id.do_transfer()

        return True


class stock_pack_operation(models.Model):

    _inherit = 'stock.pack.operation'

    scale_in = fields.Float(string="Scale In")
    scale_out = fields.Float(string="Scale Out")


class transfer_details_items(models.TransientModel):

    _inherit = 'stock.transfer_details_items'

    scale_in = fields.Float(string="Scale In")
    scale_out = fields.Float(string="Scale Out")

    @api.one
    @api.onchange('scale_in', 'scale_out')
    def update_quantity(self):
        self.quantity = self.scale_in - self.scale_out

    @api.multi
    def get_scale_in_out(self):
        self.ensure_one()
        name = 'Read Scale'
        view_id = self.env['ir.model.data'].xmlid_to_res_id(
            'crespo_personalization.view_transfer_details_items_form')
        res = {
            'name': name,
            'view_mode': 'form',
            'view_id': view_id,
            'view_type': 'form',
            'res_model': 'stock.transfer_details_items',
            'type': 'ir.actions.act_window',
            'nodestroy': True,
            'target': 'new',
            'res_id': self.id,
            'domain': '[]',
            'context': self._context
            }
        return res

    @api.multi
    def set_scale_in_out(self):
        self.ensure_one()
        return self.transfer_id.wizard_view()
