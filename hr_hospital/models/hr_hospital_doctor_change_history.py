
from odoo import models, fields


class DoctorChangeHistory(models.Model):
    _name = 'hr_hospital.doctor_change_history'
    _description = 'Doctor Change History'

    date_time = fields.Datetime(string="Date and Time", required=True,
                                default=fields.Datetime.now)
    patient_id = fields.Many2one('hr_hospital.patient',
                                 string="Patient", required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor',
                                string="Doctor", required=True)
