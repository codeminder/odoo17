
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class Diagnosis(models.Model):
    _name = 'hr_hospital.diagnosis'
    _description = 'Diagnosis'

    # Fields
    diagnosis_date = fields.Date(required=True)
    doctor_id = fields.Many2one('hr_hospital.doctor', required=True)
    patient_id = fields.Many2one('hr_hospital.patient', required=True)
    sick_id = fields.Many2one('hr_hospital.sick', required=True)
    sick_parent_id = fields.Many2one(
        related='sick_id.parent_id',
        string='Sick Type',
        store=True
    )
    treatment = fields.Text()

    mentor_comment = fields.Text(help="Comment by the mentor doctor if "
                                 "the diagnosis is made by an intern.")

    @api.onchange('doctor_id')
    def _onchange_doctor_id(self):
        """ Ensure that if the doctor is an intern,
        the mentor must be selected. """
        # Updated to `is_intern`
        if self.doctor_id and self.doctor_id.is_intern:
            if not self.doctor_id.mentor_id:
                raise ValidationError(_("Intern doctors must "
                                      "have a mentor assigned."))

    @api.model_create_multi
    def create(self, vals_list):
        """Override create to handle batch creation properly."""
        # Ensure vals_list is a list (for batch processing)
        if not isinstance(vals_list, list):
            vals_list = [vals_list]

        diagnosisis = super(Diagnosis, self).create(vals_list)
        for diagnosis in diagnosisis:
            # Updated to `is_intern`
            if (diagnosis.doctor_id.is_intern
                    and not diagnosis.mentor_comment):
                raise ValidationError(_("A mentor's comment is "
                                        "required when an intern "
                                        "makes a diagnosis."))
        return diagnosisis

    def write(self, vals):
        res = super(Diagnosis, self).write(vals)
        for record in self:
            # Updated to `is_intern`
            if record.doctor_id.is_intern and not record.mentor_comment:
                raise ValidationError(_("A mentor's comment is "
                                        "required when an intern "
                                        "makes a diagnosis."))
        return res
