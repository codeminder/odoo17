
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class AppointmentRescheduleWizard(models.TransientModel):
    _name = 'hr_hospital.appointment_reschedule_wizard'
    _description = 'Wizard to Reschedule an Appointment'

    appointment_id = fields.Many2one('hr_hospital.appointment',
                                     string='Current Appointment',
                                     required=True)
    new_doctor_id = fields.Many2one('hr_hospital.doctor',
                                    string='New Doctor', required=True)
    new_appointment_date = fields.Datetime(string='New Date', required=True)

    @api.constrains('new_appointment_date',
                    'new_appointment_time', 'new_doctor_id')
    def _check_availability(self):
        """Check that the new doctor is available at the new date and time."""
        for record in self:
            overlapping_appointments = self.env[
                'hr_hospital.appointment'].search([
                    ('doctor_id', '=', record.new_doctor_id.id),
                    ('appointment_date', '=', record.new_appointment_date),
                    ('id', '!=', record.appointment_id.id)])
            if overlapping_appointments:
                raise ValidationError(
                    _('The doctor is already booked at this time.'))

    def action_reschedule_appointment(self):
        """Reschedule the appointment by updating the doctor,
            date, and time."""
        self.appointment_id.write({
            'doctor_id': self.new_doctor_id.id,
            'appointment_date': self.new_appointment_date,
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
