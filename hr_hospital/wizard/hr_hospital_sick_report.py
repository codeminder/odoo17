from odoo import models, fields

class SickReport(models.TransientModel):
    _name = 'hr_hospital.sick_report'
    _description = 'Monthly Sick Report'

    sick_id = fields.Many2one('hr_hospital.sick', readonly=True)
    diagnosis_count = fields.Integer(string='Number of Diagnoses', readonly=True)