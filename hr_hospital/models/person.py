# -*- coding: utf-8 -*-

from odoo import models, fields

class Person(models.AbstractModel):
    _name = 'hr_hospital.person'
    _description = 'Person'
    
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    phone = fields.Char()
    email = fields.Char()
    photo = fields.Binary()
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')]
    )