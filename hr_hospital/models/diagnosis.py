from odoo import models, fields

class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    # Fields
    diagnosis_date = fields.Date(required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', required=True)
    patient_id = fields.Many2one('hr_hospital.patient', required=True)
    sick_id = fields.Many2one('hr_hospital.sick', required=True)
    treatment = fields.Text()
