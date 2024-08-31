# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError


class Appointment(models.Model):
    _name = "hr_hospital.appointment"
    _description = "Patient Appointment"

    patient_id = fields.Many2one("hr_hospital.patient",
                                 string="Patient", required=True)
    doctor_id = fields.Many2one("hr_hospital.doctor",
                                string="Doctor", required=True)
    appointment_date = fields.Datetime(required=True)
    sickness_id = fields.Many2one("hr_hospital.sick", string="Sickness")
    diagnosis_id = fields.Many2one('hr_hospital.diagnosis', string="Diagnosis")
    
    # Restrict to change appointment date for done visits
    @api.constrains('appointment_date', 'doctor_id')
    def _check_editable_fields(self):
        for record in self:
            if record.appointment_date < fields.Datetime.now():
                raise ValidationError("You cannot change the appointment date if it has already gone!")

    # Restrict delete or arch visits with diagnosises
    def unlink(self):
        for record in self:
            if record.diagnosis_id:
                raise ValidationError("You cannot delete or archive appointment with diagnosis!")
        return super(Appointment, self).unlink()
