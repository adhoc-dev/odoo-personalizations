# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class account_invoice(models.Model):

    _inherit = 'account.invoice'

    document_type = fields.Selection(
        related='journal_document_class_id.afip_document_class_id.document_type',
        readonly=True,)
