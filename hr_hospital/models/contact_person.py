# -*- coding: utf-8 -*-

from odoo import models, fields


class ContactPerson(models.Model):
    _name = 'hr_hospital.contact_person'
    _inherit = 'hr_hospital.person'
    _description = 'Contact Person'

    # Additional fields specific to Contact Person
    relationship = fields.Char(string="Ступінь спорідненості")