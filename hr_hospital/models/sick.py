# -*- coding: utf-8 -*-

from odoo import models, fields


class Sick(models.Model):
    _name = 'hr_hospital.sick'
    _description = 'Sick'

    name = fields.Char(string='Sickness Name', required=True)
    description = fields.Text()
