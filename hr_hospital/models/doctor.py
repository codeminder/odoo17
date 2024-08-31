# -*- coding: utf-8 -*-

from odoo import models, fields


class Doctor(models.Model):
    _name = "hr_hospital.doctor"
    _description = "Doctor"
    _inherit = 'hr_hospital.person'

    specialization = fields.Char()
    
    # Override name_get to call parent's name_get method
    def name_get(self):
        return super(Doctor, self).name_get()
