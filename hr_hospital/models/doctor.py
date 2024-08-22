# -*- coding: utf-8 -*-

from odoo import models, fields


class Doctor(models.Model):
    _name = "hr_hospital.doctor"
    _description = "Doctor"

    name = fields.Char(required=True)
    specialization = fields.Char()
