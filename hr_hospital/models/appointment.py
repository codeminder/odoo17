# -*- coding: utf-8 -*-

from odoo import models, fields


class Appointment(models.Model):
    _name = "hr_hospital.appointment"
    _description = "Appointment"

    patient_id = fields.Many2one("hr_hospital.patient",
                                 string="Patient", required=True)
    doctor_id = fields.Many2one("hr_hospital.doctor",
                                string="Doctor", required=True)
    appointment_date = fields.Datetime(required=True)
    sickness_id = fields.Many2one("hr_hospital.sick", string="Sickness")
