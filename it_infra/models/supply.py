# -*- coding: utf-8 -*-

from odoo import models, fields


class Supply(models.Model):

    _name = 'it_infra.supply'
    _description = 'Supply'
    _inherit = ['ir.needaction_mixin', 'mail.thread']

    name = fields.Char(
        required=True
    )

    description = fields.Text()

    supply_category_id = fields.Many2one(
        comodel_name='it_infra.supply_category',
        string='Category',
        required=True
    )

    quantity = fields.Integer()

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Provider'
    )

    device_ids = fields.Many2many(
        comodel_name='it_infra.device',
        relation='it_infra_supply_ids_device_ids_rel',
        column1='supply_id',
        column2='device_id',
        string='Devices'
    )
