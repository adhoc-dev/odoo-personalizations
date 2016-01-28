# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import models, api, _
from openerp.exceptions import Warning


class stock_picking(models.Model):
    _inherit = 'stock.picking'

    @api.one
    @api.constrains('number_of_packages')
    def validate_number_of_packages(self):
        if not self.number_of_packages > 0:
            raise Warning(_('The number of packages can not be 0'))
