# -*- coding: utf-8 -*-

from datetime import date
from odoo import api, models, fields


class Patient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Patient'
    _inherit = 'hr_hospital.person'

    birth_date = fields.Date()
    age = fields.Integer(compute='_compute_age', store=True)
    passport_data = fields.Char()
    contact_person_id = fields.Many2one('hr_hospital.contact_person')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    doctor_id = fields.Many2one('hr_hospital.doctor')
    
    @api.depends('birth_date')
    def _compute_age(self):
        """Розраховує вік пацієнта на основі дати народження."""
        for record in self:
            if record.birth_date:
                today = date.today()
                record.age = (today.year - record.birth_date.year 
                              - ((today.month, today.day) 
                                 < (record.birth_date.month, record.birth_date.day)))
            else:
                record.age = 0
