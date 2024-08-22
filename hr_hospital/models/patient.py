# -*- coding: utf-8 -*-

from odoo import models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'

    name = fields.Char(required=True)
    age = fields.Integer()
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    doctor_id = fields.Many2one('hr_hospital.doctor')
