
from odoo import models, fields


class Analysis(models.Model):
    _name = "hr_hospital.analysis"
    _description = "Patient Analysis"

    patient_id = fields.Many2one('hr_hospital.patient')
    doctor_id = fields.Many2one('hr_hospital.doctor')
    analysis_date = fields.Datetime()
    result = fields.Text()
