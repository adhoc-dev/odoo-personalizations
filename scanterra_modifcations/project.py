# -*- coding: utf-8 -*-
from openerp.osv import fields, osv


class task(osv.osv):
    _inherit = "project.task"

    _columns = {
        'name': fields.char(
            'Task Summary', size=128, required=True,
            select=True, track_visibility='onchange'),
        'date_deadline': fields.date(
            'Deadline', select=True, track_visibility='onchange'),
        'planned_hours': fields.float(
            'Initially Planned Hours', track_visibility='onchange',
            help='Estimated time to do the task, usually set by the project manager when the task is in draft state.'),
        'date_start': fields.datetime(
            'Starting Date', select=True, track_visibility='onchange'),
        'date_end': fields.datetime(
            'Ending Date', select=True, track_visibility='onchange'),
    }
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
