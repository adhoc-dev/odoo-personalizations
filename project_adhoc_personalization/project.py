# -*- coding: utf-8 -*-
##############################################################################
# For copyright and license notices, see __openerp__.py file in module root
# directory
##############################################################################
from openerp import fields, models


class project_task(models.Model):

    _inherit = 'project.task'

    deliverable = fields.Boolean(string="Deliverable")
    next_action = fields.Char(
        string="Next Action")


class project_project(models.Model):

    _inherit = 'project.project'

    project_number = fields.Char(
        related='analytic_account_id.code',
        string="Numero del Proyecto",
        readonly=True
    )
    sale_order_id = fields.Many2one(
        'sale.order',
        string="Sale order")
    partner_ids = fields.One2many(
        'res.partner',
        'project_id',
        string="Key users")
    deliverable_ids = fields.One2many(
        'project.task',
        'project_id',
        string="Deliverables",
        domain=[('deliverable', '=', True)])
    post_project_observations = fields.Text(
        string="Post Project Implementation observations")
    post_project_leader_observations = fields.Text(
        string="Post Project Observations(Customer)")
    pre_project_implementation_observations = fields.Text(
        string="Pre Project Implementation observations")
