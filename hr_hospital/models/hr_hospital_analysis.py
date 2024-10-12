
from odoo import models, fields


class Analysis(models.Model):
    _name = "hr_hospital.analysis"
    _description = "Patient Analysis"

    patient_id = fields.Many2one('hr_hospital.patient')
    doctor_id = fields.Many2one('hr_hospital.doctor')
    analysis_date = fields.Datetime()
    sample_type = fields.Selection([
        ('blood', 'Blood'),
        ('urine', 'Urine'),
        ('tissue', 'Tissue'),
        ('other', 'Other')
    ], required=True, default='blood')
    result = fields.Text()

    patient_first_name = fields.Char(
        related='patient_id.first_name', store=True)
    patient_last_name = fields.Char(related='patient_id.last_name', store=True)
    patient_phone = fields.Char(related='patient_id.phone', store=True)
