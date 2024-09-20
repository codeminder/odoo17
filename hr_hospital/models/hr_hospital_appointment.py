""" Appointment to assign a Patient meeting with Doctor """

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
    appointment_occurred = fields.Boolean(default=False)

    # Restrict to duplicat appointment date for doctor
    @api.constrains('appointment_date', 'doctor_id')
    def _check_appointment_conflict(self):
        """Ensure there are no conflicting appointments
            for the same doctor at the same time."""
        for record in self:
            conflicting_visit = self.search([
                ('doctor_id', '=', record.doctor_id.id),
                ('appointment_date', '=', record.appointment_date),
                ('id', '!=', record.id)
            ])
            if conflicting_visit:
                raise ValidationError(
                    'A doctor cannot have two appointments at the same time.')

    # Restrict to change appointment date for done visits
    @api.constrains('appointment_date', 'doctor_id')
    def _check_editable_fields(self):
        for record in self:
            if record.appointment_date < fields.Datetime.now():
                raise ValidationError(
                    "You cannot change the appointment date "
                    "if it has already gone!")

    # Restrict delete or arch visits with diagnosises
    def unlink(self):
        for record in self:
            if record.diagnosis_id:
                raise ValidationError(
                    "You cannot delete or archive appointment with diagnosis!")
        return super(Appointment, self).unlink()

    # Action for reshedule wizard
    def action_reschedule_wizard(self):
        """Open the wizard to reschedule the appointment."""
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reschedule Appointment',
            'res_model': 'hr_hospital.appointment_reschedule_wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_appointment_id': self.id},
        }
