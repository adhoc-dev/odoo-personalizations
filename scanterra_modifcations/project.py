# -*- coding: utf-8 -*-
from openerp import fields, models


class task(models.Model):
    _inherit = "project.task"

    # add track visibility
    name = fields.Char(track_visibility='onchange')
    date_deadline = fields.Date(track_visibility='onchange')
    planned_hours = fields.Float(track_visibility='onchange')
    date_start = fields.Datetime(track_visibility='onchange')
    date_end = fields.Datetime(track_visibility='onchange')

    # add custom priorities
    priority = fields.Selection(
        [('4', 'Very Low'), ('3', 'Low'), ('2', 'Medium'),
            ('1', 'Important'), ('0', 'Very important')])
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
