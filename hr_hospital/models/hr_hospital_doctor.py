
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
    intern_ids = fields.One2many('hr_hospital.doctor', 'mentor_id', string="Interns")

    # Override name_get to call parent's name_get method
    # def name_get(self):
    #     return super(Doctor, self).name_get()
