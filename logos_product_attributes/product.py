# -*- coding: utf-8 -*-
from openerp import fields, models, api


class product_template(models.Model):

    _inherit = 'product.template'

    author_id = fields.Many2one(
        'product.attribute.value',
        compute='_get_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Autor')],
        string='Autor')

    editorial_id = fields.Many2one(
        'product.attribute.value',
        compute='_get_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Editorial')],
        string='Editorial')

    collection_id = fields.Many2one(
        'product.attribute.value',
        compute='_get_attributes',
        store=True,
        domain=[('attribute_id.name', '=', 'Colección')],
        string='Colección')

    @api.one
    @api.depends(
        'attribute_line_ids',
        'attribute_line_ids.value_ids',
        'attribute_line_ids.value_ids.name',
        'attribute_line_ids.value_ids.attribute_id',
        'attribute_line_ids.value_ids.attribute_id.name',
    )
    def _get_attributes(self):
        autor_lines = self.env['product.attribute.line'].search(
            [('attribute_id.name', '=', 'Autor'),
             ('product_tmpl_id', '=', self.id)], limit=1)
        self.author_id = autor_lines.value_ids and autor_lines.value_ids[
            0] or False

        editorial_lines = self.env['product.attribute.line'].search(
            [('attribute_id.name', '=', 'Editorial'),
             ('product_tmpl_id', '=', self.id)], limit=1)
        self.editorial_id = editorial_lines.value_ids and editorial_lines.value_ids[
            0] or False

        collection_lines = self.env['product.attribute.line'].search(
            [('attribute_id.name', '=', 'Colección'),
             ('product_tmpl_id', '=', self.id)], limit=1)
        self.collection_id = collection_lines.value_ids and collection_lines.value_ids[
            0] or False


class product_attribute_value(models.Model):
    _inherit = "product.attribute.value"

    def name_get(self, cr, uid, ids, context=None):
        """Este metodo lo sobreescribimos porque no nos esta pasando en el
        contexto el show_attribute False, supongo que debe tener que ver con un
        error de la nueva api
        """
        if not context:
            context = {}
        new_context = context.copy()
        new_context['show_attribute'] = False
        return super(product_attribute_value, self).name_get(
            cr, uid, ids, context=new_context)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
