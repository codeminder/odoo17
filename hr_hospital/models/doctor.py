# -*- coding: utf-8 -*-

from odoo import models, fields


class Doctor(models.Model):
    _name = "hr_hospital.doctor"
    _description = "Doctor"
    _inherit = 'hr_hospital.person'

    name = fields.Char(required=True)
    specialization = fields.Char()
