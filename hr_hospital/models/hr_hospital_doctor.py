
from odoo import models, fields


class Doctor(models.Model):
    _name = "hr_hospital.doctor"
    _description = "Doctor"
    _inherit = 'hr_hospital.person'

    specialization = fields.Char()

    is_intern = fields.Boolean(string="Intern")
    mentor_id = fields.Many2one(
        'hr_hospital.doctor',
        string="Mentor Doctor",
        domain="[('is_intern', '=', False)]",
        help="The mentor doctor for this intern."
    )

    # Field for interns (inverse of mentor_id)
    intern_ids = fields.One2many('hr_hospital.doctor',
                                 'mentor_id', string="Interns")

    # Field for search by appointments for patients
    personal_patient_ids = fields.One2many('hr_hospital.patient',
                                           'doctor_id',
                                           string="Personal Patients")
