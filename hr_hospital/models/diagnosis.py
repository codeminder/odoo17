# -*- coding: utf-8 -*-

from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    # Fields
    diagnosis_date = fields.Date(required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', required=True)
    patient_id = fields.Many2one('hr_hospital.patient', required=True)
    sick_id = fields.Many2one('hr_hospital.sick', required=True)
    treatment = fields.Text()

    mentor_comment = fields.Text(string="Mentor Comment", help="Comment by the mentor doctor if the diagnosis is made by an intern.")

    @api.onchange('doctor_id')
    def _onchange_doctor_id(self):
        """ Ensure that if the doctor is an intern, the mentor must be selected. """
        if self.doctor_id and self.doctor_id.is_intern:  # Updated to `is_intern`
            if not self.doctor_id.mentor_id:
                raise ValidationError("Intern doctors must have a mentor assigned.")

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to handle batch creation properly."""
        # Ensure vals_list is a list (for batch processing)
        if not isinstance(vals_list, list):
            vals_list = [vals_list]
            
        diagnosisis = super(Diagnosis, self).create(vals_list)
        for diagnosis in diagnosisis:
            if diagnosis.doctor_id.is_intern and not diagnosis.mentor_comment:  # Updated to `is_intern`
                raise ValidationError("A mentor's comment is required when an intern makes a diagnosis.")
        return diagnosisis

    def write(self, vals):
        res = super(Diagnosis, self).write(vals)
        for record in self:
            if record.doctor_id.is_intern and not record.mentor_comment:  # Updated to `is_intern`
                raise ValidationError("A mentor's comment is required when an intern makes a diagnosis.")
        return res