# -*- coding: utf-8 -*-
from openerp import fields, models, api


class task(models.Model):
    _inherit = "project.task"

    # add track visibility
    name = fields.Char(track_visibility='onchange')
    date_deadline = fields.Date(track_visibility='onchange')
    planned_hours = fields.Float(track_visibility='onchange')
    date_start = fields.Datetime(track_visibility='onchange')
    date_end = fields.Datetime(track_visibility='onchange')

    # add custom priorities
    priority = fields.Selection([
        ('0', 'Very Low'),
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'Important'),
        ('4', 'Very important'),
        # ('0', 'Very important'),
        # ('1', 'Important'),
        # ('2', 'Medium'),
        # ('3', 'Low'),
        # ('4', 'Very Low'),
        ])

    @api.multi
    def write(self, vals):
        if vals.get('user_id') and 'date_start' not in vals:
            for line in self:
                vals['date_start'] = line.date_start
                super(task, line).write(vals)
            return True
        return super(task, self).write(vals)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
