# -*- coding: utf-8 -*-
from odoo import api, fields, models

class partnerDate(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'

    date = fields.Date(
        string='Fecha',
    )
